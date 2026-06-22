import math

def area_of_circle(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius = 5
    result = area_of_circle(radius)
    print(result)