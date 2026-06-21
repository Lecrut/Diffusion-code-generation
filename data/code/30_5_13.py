import math

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    r = 5
    area = circle_area(r)
    print(area)