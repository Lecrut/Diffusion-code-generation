import math

def calculate_circle_perimeter():
    radius = 100
    perimeter = 2 * math.pi * radius
    return float(perimeter)

if __name__ == '__main__':
    print(calculate_circle_perimeter())