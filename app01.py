print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is 34 + 2?")
  print("   a) 32")
  print("   b) 24")
  print("   c) 36")
  print("   d) 17")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. :( "
    score -=1
  elif answer == "b":
    output = "Wrong. :( "
    score -=1
  elif answer == "c":
    output = "Yes, that's right! :D"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. :( "
    score -=1
  else:
    output = "Please choose a, b, c or d only,noob."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "The chemical formula H2 represents")
  print("   a) one hydrogen molecule")
  print("   b) two hydrogen atoms")
  print("   c) one hydrogen atom")
  print("   d) two hydrogen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right! :D "
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. noob. If so, then it will be written as H and H - two hydrogen atoms."
    score -=1
  elif answer == "c":
    output = "Wrong. noob. Clearly the number 2 in the formulae must mean something?"
    score -=1
    
  elif answer == "d":
    output = "Wrong. noob. What's the difference between a molecule and an atom?"
    score -=1
  else:
    output = "Please choose a, b, c or d only, noob. "

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is my favourite canteen food? ")
  print("   a) mushroom minced meet noodles")
  print("   b) ramen and beef")
  print("   c) chicken cutlet")
  print("   d) udon")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again. :) "
    score -=1
  elif answer == "b":
    output = "Wrong. Think again. :)"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again. :)"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only, noob."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
  
