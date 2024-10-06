import subprocess
import sys

def main():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'setuptools', 'wheel'])
    subprocess.check_call([sys.executable, 'setup.py', 'sdist', 'bdist_wheel'])

if __name__ == '__main__':
    main()
