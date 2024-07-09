import turtle
import random

s = turtle.Screen()
s.title('Primer proyecto')
s.bgcolor('gray')


Jugador1 = turtle.Turtle()
Jugador2 = turtle.Turtle()

#modificar los jugadores
#para que no se vea que las tortugas hacen su meta
Jugador1.hideturtle()
Jugador1.shape('turtle')
Jugador1.color('red', 'red')
Jugador1.shapesize(2,2,2)
Jugador1.pensize(3)

#para que no se vea que las tortugas hacen su meta
Jugador2.hideturtle()
Jugador2.shape('turtle')
Jugador2.color('blue', 'blue')
Jugador2.shapesize(2,2,2)
Jugador2.pensize(3)

#dibujas las metas
Jugador1.penup()
Jugador1.goto(200,200)
Jugador1.pendown()
Jugador1.circle(40)

#ahora la ponemos en la linea de salida
Jugador1.penup()
Jugador1.goto(-250, 225)

#mostramos la tortuga
Jugador1.showturtle()

Jugador2.penup()
Jugador2.goto(200, -200)
Jugador2.pendown()
Jugador2.circle(40)

Jugador2.penup()
Jugador2.goto(-250, -170)

#mostramos la tortuga
Jugador2.showturtle()

dado = [1,2,3,4,5,6]

#ponemos la condicion par aque el juego se detenga cuando una tortuga llegue a su casa
for i in range(20):
    if Jugador1.pos() >= (180,200):
        print('La tortuga roja ha ganado!')
        break
    elif Jugador2.pos() >=(180,-200):
        print('La tortuga azul ha ganado!')
        break
    else:
        turno1 = input('presiona la tecla enter para avanzar la tortuga roja')
        turno1 = random.choice(dado)
        print('tu numero es: ', turno1, "\navanzas: ", turno1*20)
        Jugador1.pendown()
        Jugador1.fd(20*turno1)

        turno2 = input('presiona la tecla enter para avanzar la tortuga azul')
        turno2 = random.choice(dado)
        print('tu numero es: ', turno2, "\navanzas: ", turno2*20)
        Jugador2.pendown()
        Jugador2.fd(20*turno2)

turtle.done()
