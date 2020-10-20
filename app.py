print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling. Life is good!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find new hobbies to do or go out! or sleep!")
      counter += 1
    if each_word == "tiring":
      feelings_list.append("tiring")
      encouragement_list.append("Git sum sleep boiiii!")
      counter += 1
    if each_word == "hungry":
      feelings_list.append("hungry")
      encouragement_list.append("the canteen got your back ;)!")
      counter += 1
    if each_word == "heartbroken":
      feelings_list.append("heartbroken")
      encouragement_list.append("You can finally date someone who is better!!")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("I am here whenever you are ready to talk:)")
      counter += 1   
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("That’s never happened to me, but I can really get why you’re feeling that way.")
      counter += 1   
    if each_word == "empty":
      feelings_list.append("empty")
      encouragement_list.append("You will never succeed in killing yourself")
      counter += 1   
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
