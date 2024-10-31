'''
The above code is a Python implementation of a turtle race game. The user is prompted to enter their bet on the winning turtle's color. 

First, the necessary modules (Turtle and Screen) are imported. The
screen is then set up with a height of 400 and width of 500. A prompt is
displayed to ask the user to enter their bet on the winning turtle's
color. The colors list contains the colors of the six turtles in the
race, and the y_positions list contains the vertical starting positions
for the turtles.

In the for loop, six turtles are created with a different color assigned
to each based on the 'colours' list. The turtles are then moved to their
starting positions with y-coordinates based on the 'y_positions' list.
All six turtles are added to the 'all_turtles' list for ease of access.

If the user enters a bet on the winning turtle, the 'race_active'
variable is set to True, which begins the turtle race.

In the while loop, the turtles move forward by a random distance
(between 0 and 10 pixels) until one turtle reaches the x-position of
230, indicating the winner. Once the winner is determined, the
'race_active' variable is set to False, and the winning turtle's color
is assigned to the 'winning_colour' variable. If the winning colour is
the same as the user's bet, the user is notified with the message "You
win!" and the winning color. If the winning color is not the user's bet,
the message "You lose." and the winning turtle's color are displayed.

Finally, the GUI window can be closed by clicking on the window, thanks to 'screen.exitonclick()'.
'''

from turtle import Turtle, Screen
import random

# Set up the initial variables for the turtle race
race_active = False
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user for their bet on the winning turtle's color
turtle_bet = screen.textinput(title="Make your bet!", prompt="Which turtle do you think will win(red,orange,yellow,pink,blue,purple)? \n Enter a colour: ")

# Set up the turtle colors and starting positions
colours = ["red", "orange", "yellow", "pink", "blue", "purple"]
y_positions = (-100, -60, -20, 20, 60, 100)
all_turtles = []

# Initialize the six turtles and add them to the 'all_turtles' list
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=(y_positions[turtle_index]))
    all_turtles.append(new_turtle)

# Start the turtle race if the user has entered a bet
if turtle_bet:
    race_active = True

# Move the turtles randomly until one reaches the finish line
while race_active:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # Stop the race and determine the winner when a turtle has crossed the finish line
            race_active = False
            winning_colour = turtle.pencolor()
            if winning_colour == turtle_bet:
                # Notify the user if they guessed the winning turtle's color correctly
                print(f"You win! The {winning_colour} turtle is the winner.")
            else:
                # Notify the user if they did not guess the winning turtle's color correctly
                print(f"You lose. The {winning_colour} turtle is the winner.")

        # Move each turtle randomly forward between 0 and 10 pixels
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Wait for the user to close the window before ending the program
screen.exitonclick()
