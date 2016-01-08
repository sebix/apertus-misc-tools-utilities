#!/usr/bin/python2

# Add a synthetic black line to a TI3 file generated by scanin
# (troy_s told me to do that :P)

import os, sys, re

if len(sys.argv) == 1:
    print "Usage: python2 %s file.ti3" % sys.argv[0]
    raise SystemExit

f = open(sys.argv[1], "r")
inp = f.readlines()
f.close()

black_line = "00B 0 0 0 0 0 0 0 0 0"

for l in inp:
    if l.strip() == black_line:
        print "Synthetic black already there, nothing to do."
        raise SystemExit

f = open(sys.argv[1], "w")

for l in inp:
    m = re.match("NUMBER_OF_SETS +([0-9]+) *$", l)
    if m:
        n = int(m.groups()[0])
        print >> f, "NUMBER_OF_SETS %d" % (n+1)
        continue
    
    print >> f, l.strip()

    if l.strip() == "BEGIN_DATA":
        print >> f, black_line
        print "Synthetic black added to %s." % sys.argv[1]

f.close()
