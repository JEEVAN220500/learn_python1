#Input Collection: Prompt the user to enter the player's name and store it as a string
#Numeric Input Processing: Accept the number of games played and convert it to an integer data type
#Score Data Entry: Collect the total score achieved and store it as an integer
#Computation: Calculate the average score per game using division
#Output Display: Present the results in the specified format shown below
#Expected Output Format

#Player: <name>

#Games Played: <number>

#Total Score: <score>

#Average Score: <average>

name = input("Player:")
games_played = int(input("Games Played:"))
total_score = int(input("Total Score:"))
avg_score = print(f"Average Score for {name}: {total_score // games_played}")