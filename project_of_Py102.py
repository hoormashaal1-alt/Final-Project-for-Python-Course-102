from datetime import datetime, date 
people=[]
while(True):
  name=input("Enter the name or enter stop to leave ").strip()
  if name.lower()=="stop":
    break
  
  age=input("Enter the age ")
  if age.lower()=="stop":
   print("you must to enter ",name," age, please enter the name again and the" \
   " correct age")
   continue
  
  try:
    dob=datetime.strptime(age, "%d-%m-%Y").date()
  except ValueError:
    print("You entered wrong date!")
    continue

  today=date.today()
  theAge=today.year-dob.year
  people.append((name,theAge,dob))

for name,theAge,dob in people:
  print(name+" is ",theAge," and he/she born on ",dob.strftime("%A"))
  
print("the youngest is ", max(people, key=lambda x: x[2]))
print("the olest is ", min(people, key=lambda x: x[2]))
print("the total number of people you entered is ",len(people))
 

  

  
  






