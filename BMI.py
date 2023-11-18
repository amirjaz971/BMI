not_closed=True


while not_closed:
   
      try:
     

       weight=int(input("enter your weight in kg: "))
       height=int(input("enter your height in meter: "))
      except ValueError:
       print("invalid value!")
       continue 
      if weight>0 and height>0:
         height=height/100
         bmi=weight/(height**2)
         print("your bmi is:",bmi)
         if bmi<18.5:
            print("you are having an under weight")
         elif 18.5<=bmi<25:
            print("you are having a normal weight")
         elif 25<=bmi<30:
            print("you are having an over weight")
         elif 30<=bmi<35:
            print("you are having an obesity(class1)")  
         elif 35<=bmi<40:
            print("you are having an obesity(class2)")   
         else:
            print("you are having an extreme obesity!")       
      else:
         print("wrong values!")
      
      while True:
       answer=input("do you want to continue?(Y/N): ")   
       if answer.lower()=="y":
          break
       elif answer.lower()=="n":
          not_closed=False
          break
       else:
          print("invalid value!")
          






 
       
print("good-bye")