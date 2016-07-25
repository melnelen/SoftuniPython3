import turtle

length = int(input('Enter square length > '))

turtle.speed('slow')

for i in range(4):
    turtle.forward(length)
    turtle.right(90)

turtle.done()

# test
