import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    radius = 10.5
    perimeter = calculate_circle_perimeter(radius)
    print(perimeter)