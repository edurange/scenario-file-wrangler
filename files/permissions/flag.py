#! /usr/bin/python -E

import os.path
import stat

def checkperms(filenme):
    st = os.stat(curDir + '/' + filenme)
    oct_perm = oct(st.st_mode)
    perms = int(str(oct_perm[-3]) + str(oct_perm[-2]) + str(oct_perm[-1]))
    return perms

curDir = os.getcwd()

def verifyCompletion():
    perm1 = False
    copied_perm1 = False
    perm2 = False
    copied_perm2 = False

    #Check for files
    if (os.path.exists(curDir + '/perm1.txt')):
        perm1 = True

    if (os.path.exists(curDir + '/copied_perm1.txt')):
        # If copied_perm1.txt is present and the permissions are correct, BOOL flag is set to true
        if checkperms('copied_perm1.txt') == 660:
            copied_perm1 = True

    if (os.path.exists(curDir + '/perm2.txt')):
        # If file2 still exists, BOOL flag set to true
        perm2 = True

    if (os.path.exists(curDir + '/copied_perm2.txt')):
        # If copied_perm2.txt exists and the permissions are correct, BOOL flag set to true
        if checkperms('copied_perm2.txt') == 764:
            copied_perm2 = True

    return perm1 + copied_perm1 + perm2 + copied_perm2

if verifyCompletion() == 2:
    # Check for files
    codeDir = curDir.replace('permissions', 'codes')
    filepath = codeDir + '/permissions.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            print line.strip()
            line = fp.readline()
else:
    print "Not quite. Re-read the instructions. You should have perm1.txt, copied_perm1.txt, perm2.txt and copied_perm2.txt in the directory. Use chmod to change the permissions as instructed."
