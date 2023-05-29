#numbers are based on the action. It goes from a 1-5 scale. If it is a low curiosity action, the number will be 1. If it is a high curiosity action, the number will be 5. It'll be 3 if it's a medium curiosity action. 

#A total curiosity score above 10 indicates that he/she falls under the high-curiosity category, while below 10 indicates that they're in the low-curiosity category. 

#Put values to determine the weightage of each action type that you are addressing.
actionscores = {
  "Watch Video": 5,
  "Ask question": 5,
  "Read link": 3,
  "Studying": 5
}

#Set up a dictionary to track the user count and the weightage of each action type.
curiosityinformation = {action: {"UserCount": 0, "Weightage": 0} for action in actionscores}

#Call the function to be able to track user actions and weightage.
def trackcuriosity(action):
  if action in actionscores:
    curiosityinformation[action]["UserCount"] += 1
    curiosityinformation[action]["Weightage"] += actionscores[action]


#implement the 'trackcuriosity()' function. It passes the action type as an argument.
trackcuriosity("Watch Video")
trackcuriosity("Ask question")
trackcuriosity("Read link")
trackcuriosity("Studying")

#Print the curiosity data. I used the 'curiosityinformation' dictionary to understand the used count and weightage of each type to better understand where the person's curiosity levels are. 
for action, data in curiosityinformation.items():
  print(action.capitalize())
  print("User Count:", data["UserCount"])
  print("Weight:", data["Weightage"])
  print()

#This is to categorize the types of people based on tracing curiosity levels
if data["Weightage"] >=5:
  print("High curiosity person");
#if data["Weightage"] <= 10: print("Medium curiosity person");
if data["Weightage"] < 5:
  print("Low curiosity person");
  

#This curiosity indicator allows us to evaluate curiosity based on the frequency and the importance of user actions. We can track the cumulative weight with each action type and the count of users.