from math import pi

def circle_area(radius):
    return pi * radius ** 2

if __name__ == '__main__':
    print(circle_area(5))
    print(circle_area(1))
    print(circle_area(0))