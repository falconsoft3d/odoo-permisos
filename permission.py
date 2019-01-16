# -*- coding: utf-8 -*-

# web: http://falconsolutions.cl
# auth: Marlon Falcon
# company: falconsolutions
# creation date: 15-01-2019
# modification date: 15-01-2019
# version: 1.0.0

from os import listdir, path


def create_ir_model_access():
    """."""
    f = open('./security/ir.model.access.csv', 'w')
    f.write(
        'id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n')
    f.close()

necessary_folder = ['models', 'security']
models = []

for folder in necessary_folder:
    if folder not in listdir('.'):
        print('Es necesario: {}'.format(folder))
        exit()

if 'ir.model.access.csv' not in listdir('./security'):
    create_ir_model_access()

for py in listdir('./models'):
    file_extension = path.splitext(py)[-1]
    if file_extension == '.py' and py != '__init__.py':
        with open('./models/' + py) as lines:
            for line in lines:
                if '_name' in line.split(' '):
                    model = line.replace(
                        ' ', '').replace(
                        "'", '"').split(
                        '="')
                    model = model[-1].replace(
                        '"', '').replace(
                        '\n', '').replace(
                        '\r', '')
                    models.append(model)

group_id = raw_input('Ingresa el nombre del grupo --> ')
prefix = raw_input('Ingresa el prefijo del grupo --> ')
perm_read = raw_input('Leer:     0/1 --> ')
perm_write = raw_input('Escribir: 0/1 --> ')
perm_create = raw_input('Crear:    0/1 --> ')
perm_unlink = raw_input('Eliminar: 0/1 --> ')
models = list(set(models))

f = open('./security/ir.model.access.csv', 'a')
for model in models:
    line = "access_{model}_{prefix},{model1},model_{model},{group_id},{perm_read},{perm_write},{perm_create},{perm_unlink}".format(
        prefix=prefix,
        model1=model,
        model=model.replace('.', '_'),
        group_id=group_id,
        perm_read=perm_read,
        perm_write=perm_write,
        perm_create=perm_create,
        perm_unlink=perm_unlink)
    f.write(line + '\n')

f.close()
print "\n*** Permisos creados para: {} ***\n".format(group_id)
