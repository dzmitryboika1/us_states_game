import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
picture = "blank_states_img.gif"
screen.bgpic(picture)

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")

guessed_states = []
while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{guessed_states}/50 States Correct",
                                     prompt="What's another state name?").title()
    if answer_states == "Exit":
        all_states_list = data.state.to_list()
        states_to_learn = sorted(list(set(all_states_list) - set(guessed_states)))
        states_to_learn = pandas.DataFrame(states_to_learn)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_states in data.state.unique():
        guessed_states.append(answer_states)
        coord = data[data.state == answer_states]
        turtle.goto(int(coord.x), int(coord.y))
        turtle.write(f"{answer_states}", font=('Arial', 8, 'normal'))
