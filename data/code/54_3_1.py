import math
def get_area(radius):
    return math.pi * radius**2
if __name__ == '__main__':
    print(get_area(5.0))
    print(get_area(0.0))
    print(get_area(1.5))