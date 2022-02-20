from distutils.command.config import config
from msilib.schema import File
from xml.etree.ElementPath import find
from matplotlib.cbook import print_cycles


def main():
    open("/path/to/mars.jpg")
    
if __name__ == '_main_':
    main()
    
>>> try:
...    open('Config.txt')
... except FileNotFoundError:
...     print("Couldn't find the config.txt file")
...
Couldn't find the config.txt file!
        
