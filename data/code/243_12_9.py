import math

CIRCLE_PERIMETER_MULTIPLIER = math.pi

def circle_perimeter(diameter):
    return diameter * CIRCLE_PERIMETER_MULTIPLIER

if __name__ == '__main__':
    sample_diameter = 25
    print(circle_perimeter(sample_diameter))