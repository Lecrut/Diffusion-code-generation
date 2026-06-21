import math
PI = math.pi

def circle_area(radius):
    if radius <= 0:
        return 0
    return PI * (radius * radius)

if __name__ == '__main__':
    print(circle_area(3.0))