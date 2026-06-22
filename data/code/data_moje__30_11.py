import math

def calculate_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius = 5
    result = calculate_area(radius)
    print(result)