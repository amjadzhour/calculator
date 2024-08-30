from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
Builder.load_file('calculator.kv')

class calculator1(Widget):
        o=[]
        def AC(self):
               self.ids.text1.text=''
               self.o=[]

        def C(self):
               self.ids.text1.text=''
               self.o=[]
        def five(self):
               self.ids.text1.text+='%'
               self.o.append('%')  

        def numU(self):
                 if self.ids.text1.text!="" and len(self.o)<3 :  
                  self.ids.text1.text+='/'
                  self.o.append('/') 

        def num7(self):
               self.ids.text1.text+='7'

        def num8(self):
               self.ids.text1.text+='8' 

        def num9(self):
               self.ids.text1.text+='9'   

        def num7(self):
               self.ids.text1.text+='7'   

        def x5(self):
               if self.ids.text1.text!="" and len(self.o)<3:  
                 self.ids.text1.text+='X'
                 self.o.append('X')       

        def num4(self):
               self.ids.text1.text+='4' 

        def num5(self):
               self.ids.text1.text+='5'

        def num6(self):
               self.ids.text1.text+='6'


        def numy(self):
               if len(self.o)>=2 and self.o[1]!='X' and self.o[1]!="/":
                  self.ids.text1.text=self.ids.text1.text.replace(self.o[1],'-') 
                  self.o[1]='+'
               elif len(self.o)<3 :
                 self.ids.text1.text+='-'
                 self.o.append('-')  
                     
        


        
        def num1(self):
               self.ids.text1.text+='1'  

        
        def num2(self):
               self.ids.text1.text+='2'

        
        def num3(self):
               self.ids.text1.text+='3'  

        def plus(self):
              if len(self.o)==2 and self.o[1]!='X' and self.o[1]!="/":
                  self.ids.text1.text=self.ids.text1.text.replace(self.o[1],'+') 
                  self.o[1]='+'
              elif len(self.o)<3 :  
                 self.ids.text1.text+='+'
                 self.o.append('+')  

        def num_dout(self):
                self.ids.text1.text+='.'  

        def num0(self):
               self.ids.text1.text+='0'      


        def factoral1(self):
               self.ids.text1.text+='!' 
               self.o="!" 
       
        def factoral(self,num):
            if num >=0:  
              f=1
              for i in range(1,(num+1),1):
                     f*=i
              return f 
       
        def h(self):
            return  len(self.o)==1  
        def check(self):
             return self.o[0]==self.o[1]  

        def num_equal(self):
             lis=self.ids.text1.text
             e=0
             if self.h():
               try:
                     o=self.o[0]  
                     if o=='%':
                        lis=lis.split("%")
                        e=float(lis[0]) % float(lis[1])

                     elif o=='/':
                        lis=lis.split("/")
                        e=float(lis[0]) /float(lis[1])
                     elif o=='X':
                        lis=lis.split("X")
                        e=float(lis[0]) * float(lis[1])   
                     elif o=='-': 
                        lis=lis.split("-")
                        print(lis)
                        e=float(lis[0]) - float(lis[1])
                                  
                     elif o=='+':
                        lis=lis.split("+")
                        
                        print(lis)
                        e=float(lis[0]) + float(lis[1])

                     elif o=='!':
                        lis=lis.split("!")
                        e=self.factoral(int(lis[0]))    

                     self.ids.text1.text=str(e)    
                     self.o=[]
               except Exception:
                      print(Exception)   
             elif self.h()!=True: 
                    try:
                     o=self.o[1]  
                     l=self.o[0]
                     if o=='/':
                            lis=lis.split(self.o[1])
                            e=float((lis[0])) /float(lis[1])
           

                     elif o=='X':
                          
                            lis=lis.split(self.o[1])
                            e=float((lis[0])) * float(lis[1])  
                             
                     

                     elif o=='-': 
                       if self.check()!=True:  
                            lis=lis.split(self.o[1])
                            print(lis)
                            e=float((lis[0])) - float(lis[1])
                       else:
                            lis=lis.split(self.o[1])
                            print(lis)
                            e=float((l+lis[1])) - float(lis[2])
                                  
                     elif o=='+':
                       if self.check()!=True: 
                            lis=lis.split(self.o[1])
                            print(lis)
                            e=float((lis[0])) + float(lis[1])  
                       else:
                            lis=lis.split(self.o[1])
                            print(lis)
                            e=float(l+(lis[1])) + float(lis[2])  

                     self.ids.text1.text=str(e)    
                     self.o=[]
                    except Exception:
                      print(Exception)      


class calculator(App):
        def build(self):
                return calculator1()
        

if __name__=="__main__":
    calculator().run()
