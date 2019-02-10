import re
import sys

in_file = open(sys.argv[1]).read()
matches = re.findall('<gpxx:Temperature>([-0-9\.]+)</gpxx:Temperature>', in_file)
if len(matches) == 0:
    print "No temperatures found."
    sys.exit(1)
temps = [float(i) for i in matches]
print "Max. temp is %.1f and min. temp is %.1f." % ( max(temps), min(temps))
