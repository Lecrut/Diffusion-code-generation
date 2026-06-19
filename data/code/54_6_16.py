from math import pi

def circle_area(r):
    return pi * (r ** 2)

if __name__ == '__main__':
    radius = 3
    print(circle_area(radius))