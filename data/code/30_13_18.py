from math import pi

def circle_area(r):
    return pi * r ** 2

if __name__ == '__main__':
    print(circle_area(5))
    print(circle_area(1))
    print(circle_area(0))