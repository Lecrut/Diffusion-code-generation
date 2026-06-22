import math

def circle_perimeter(diameter):
    PERIMETER_FACTOR = math.pi
    return diameter * PERIMETER_FACTOR

if __name__ == '__main__':
    sample_diameter = 25
    perimeter = circle_perimeter(sample_diameter)
    print(perimeter)