import math

def circle_perimeter(diameter):
    return diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 40
    perimeter = circle_perimeter(sample_diameter)
    print(perimeter)