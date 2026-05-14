heads_="""
using System;
using System.Threading;


public class Games{   
    static int score=0;
    static int fire=0;
    static int live=0;
    static int lives=3;
    static int x=0;
    static int y=0;
    static int z=0;
    static int w=0;
    static int h=0;
    static bool ends=false;
    static int camera=0;
    static int enemy=0;
    static int enemycount=3;
    
    static int tsleep=100;
    
    static void debugs(String c){
       Console.WriteLine(c);
       Thread.Sleep(100);
    }

"""
def saves(files,mode,value):
    f1=open(files,mode)
    f1.write(value)
    f1.close()


def heads(files,value):
    saves(files,"w",value)

print("give me the file name .txt ? ")
filesa=input().strip()


def getfiles(files):
    f1=open(files,"r")
    values=f1.read()
    f1.close()
    v=values.split("\n")
    return v
    

def defs(files,value):
    print("handle : function :"+value)
    saves(files,"a",(" "*4))
    saves(files,"a","static void ")
    saves(files,"a",value)
    saves(files,"a"," (){\n")
    saves(files,"a",(" "*8)+"//put you code here\n")
    saves(files,"a",(" "*8)+ "debugs(\"")
    saves(files,"a",value)
    saves(files,"a","\");\n}\n")

print(filesa)
gfiles=getfiles(filesa)

filesa="Program.cs"
heads(filesa,heads_)
for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs(filesa,sss)


heads__="""
    static void mainloop(){
        //put you code here
        debugs("mainloop");
        while(true){

"""

def defs_(files,value):
    print("handle : function :"+value)
    saves(files,"a","\n"+" "*12)
    
    saves(files,"a",value)
    saves(files,"a","();\n")

saves(filesa,"a",heads__)

for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs_(filesa,sss)

heads___="""
            if (ends)break;
        }
        
    }
    
    static void setuploop(){
        //put you code here
        debugs("setuploop");
        while(true){
           mainloop();
           if (ends)break;
        }
        
        
    }
    static void Main(String[] arg){
        //put you code here
        debugs("main");
        setuploop();
    
        
    }
}

"""
saves(filesa,"a",heads___)