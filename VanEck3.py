# This is the Python3 version of VanEck.py

import sys
sequence = [0]
seen = []
id = 0
max = 10

# check command line args
arg_list = 0
arg_seen = 0
arg_info = 0

def printHelp():
    print("\n======= ARGUMENT HELP =======")
    print("filename.py -l -s -h -n <x>")
    print("   -l   : prints the VanEck Sequence generated")
    print("   -s   : prints integers seen at any point in the sequence")
    print("   -i   : prints info about the sequence at the end")
    print("   -h   : prints this help message")
    print(" -n <x> : used to set program to gen x of places to generate in the sequence (Default 10)")

if (len(sys.argv) == 1):
    printHelp()

for arg in sys.argv:
    if arg == "-s":
        arg_seen = 1
    elif arg == "-l":
        arg_list = 1
    elif arg == "-h":
        printHelp()
    elif arg == "-i":
        arg_info = 1
    elif arg == "-n":
        ind = (sys.argv.index("-n")) + 1
        if (int(sys.argv[ind]) > 0):
            max = int(sys.argv[ind])
        else:
            print("Input is less than or equal to 0; Using default")
            max = 10


def used(num):
    ret = 0
    for x in sequence:
        if x == num:
            ret += 1
    return ret

def when(num):
    vis = []
    val = 0
    i = 0

    while i < len(sequence):
        if sequence[i] == num:
            vis.append(i)
        i += 1

    val = (vis[len(vis)-1]) - (vis[len(vis)-2])

    return val

while id < max:
    if used(sequence[id]) == 1:
        sequence.append(0)
        seen.append(sequence[id])
    else:
        sequence.append(when(sequence[id]))
    id += 1

if arg_list == 1:
    print("\n======= SEQUENCE =======")
    for num in sequence:
        print("%i,") %num,
    else:
        print

if arg_seen == 1:
    print("\n===== USED NUMBERS =====")
    seen.sort()
    for num in seen:
        print("%i,") %num,
    else:
        print

if arg_info == 1:
    print("\n========= INFO =========")
    print("Sequence was %i values long, having %i unique integers in the sequence.") % (max,len(seen))
