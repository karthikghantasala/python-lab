import os

os.system('ls -l')

with open('ns-kovan.txt') as f:
   for line in f:
       # For Python3, use print(line)
       print line
       kubecommand = "kubectl delete ns " + line
       os.system(kubecommand)
       if 'str' in line:
          break

#myfile = open("ns-kovan.txt", "r")
#myline = myfile.readline()
#print(myline)
#myfile.close()

