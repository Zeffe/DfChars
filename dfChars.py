import urllib, urllib2
import thread
import os, time

panera = []
tested = []

dicks = False
step = 1 # Amount of numbers to add each time it checks

def _cPH(var, dik):
        try:
                get = urllib2.urlopen("http://www.dragonfable.com/df-chardetail.asp?id=" + str(var))
                handleData = get.read()
                get.close()
                exist = 'Character not Found'
                if exist not in handleData:
                        _lvl = handleData.split("&Level=")[1].split("&")[0]
                        _name = handleData.split("'Name=")[1].split('&')[0]
                        _name = _name.split()
                        name = ""
                        for i in _name:
                            name += i + " "
                        out = ""
                        out = str(var) + ":" + name[0:len(name) - 1].replace("%27", "'") + ":" + _lvl
                        _file = open("DfChars.txt", "a")
                        _file.write(out + "\r\n")
                        _file.close
                        panera.append(var)
                        print "[+] " + str(var)
                else:
                        print "[-] " + str(var)
                tested.append(var)
        except:
                _file = open("DfChars.txt", "a")
                _file.write("ERRORED OUT ON" + str(var) + "\r\n")
                _file.close

_dicks = 0
while not dicks:
        if _dicks == 0:
                _var = raw_input("Starting number: ")
                try:
                        _var = int(_var)
                        _dicks += 1
                        dicks = not dicks
                except:
                        print 'Not a valid number.'

while True:
    if _var not in tested:
        thread.start_new_thread(_cPH, (_var, _dicks))
        time.sleep(int(150)/float(1000))
    _var += 1

print ""
print ""
print "Found " + str(len(work)) + " working numbers."
print "Tested " + str(len(tested)) + "."
print "Ended on " + str(_var - 1)

raw_input()
