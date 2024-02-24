import glob

to_version = '3.4'
outfile = 'update.bat'

files = glob.glob('*.prj')
with open(outfile, 'w') as fp:
    for file in files:
        fp.write('"C:\\Program Files (x86)\\NIST\\CONTAM 3.4.0.4\\prjup.exe" -n -p %s %s\n' % (to_version, file))
