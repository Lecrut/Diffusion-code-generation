import math

def calculate_circle_perimeter(diameter):
    return diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 25
    perimeter = calculate_circle_perimeter(sample_diameter)
    print(perimeter)