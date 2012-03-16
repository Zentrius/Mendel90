import os
import sys
import shutil

def render(machine):
	render_dir = machine + os.sep + "render"
	print render_dir 
	try:
		os.stat(render_dir)
	except:
		os.mkdir(render_dir)
	li = os.listdir(machine+os.sep+'stls')
	stls = []
	for i in li:
		stls.append(i[:-4])
	for i in stls:
		command = 'blender utils'+os.sep+'render.blender -P utils'+os.sep+'viz.py -- '+machine+os.sep+'stls'+os.sep+i+'.stl '+machine+os.sep+'render'+os.sep+i+'.png'
		print command

if __name__ == '__main__':
    if len(sys.argv) > 1:
        render(sys.argv[1])
    else:
        print "usage: bom [mendel|sturdy|your_machine]"
        sys.exit(1)
