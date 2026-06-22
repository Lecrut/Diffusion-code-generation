import math

def calculate_circle_perimeter():
    radius = 100
    pi = math.pi
    perimeter = 2 * pi * radius
    return float(perimeter)

if __name__ == '__main__':
    result = calculate_circle_perimeter()
    print(result)