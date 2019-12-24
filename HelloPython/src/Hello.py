'''
Created on Dec 8, 2017

@author: Stephen
'''
import json

class World:
    name = "World"
    
    def Hello(self):
        return("Hello Git " + self.name)
        
    def Goodbye(self):
        return("Goodbye Git " + self.name)
        
if __name__ == '__main__':
    print("hello, Python!")
    
    a, b = 0, 1
    while a < 10:
        print(a, b)
        a, b = b, a + b
        
    x = World()
    print(x.Hello())
    j = {'file':'recordingfile',"title":"NCIS","subtitle":"Episode 1"}
    print(json.dumps(j))

    with open('output/hellofile.txt', 'w') as f:
        f.write(x.Hello())
        f.write('\n')
        f.write(x.Goodbye())
    with open('output/hellofile.txt', 'r') as f:
        while True:
            s = f.readline()
            if s == '':
                break
            print(s)