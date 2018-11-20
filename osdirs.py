import os
import tkinter.filedialog as fd
dirname=fd.askdirectory()
def f1(dirname):
  os.chdir(dirname)
                #l=[os.path.abspath(f)for f in os.listdir()]
  for f in os.listdir():
        if os.path.isfile(f):
          print(os.path.abspath(f))
        else:
          f1(f)
    
f1(dirname)
