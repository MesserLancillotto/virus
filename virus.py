from turtle import *


def main():
    speed(20)
    color("cyan")
    bgcolor("black")
    b = 200
    while b > 0:
        left(b)
        forward(b*3)
        b -= 1
    done()


if __name__ == "__main__":
    main()
