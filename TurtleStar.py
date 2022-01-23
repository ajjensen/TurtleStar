import turtle
import tkinter

turtle.TurtleScreen(tkinter.Canvas())

for i  in range(0, 5):
    turtle.forward(250)
    turtle.right(180 - 36)

turtle.mainloop()