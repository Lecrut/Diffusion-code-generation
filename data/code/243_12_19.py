import math

def validate_diameter(diameter):
    if not isinstance(diameter, (int, float)) or diameter <= 0:
        raise ValueError("Diameter must be a positive number")

def circle_perimeter(diameter):
    validate_diameter(diameter)
    return diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 25
    perimeter = circle_perimeter(sample_diameter)
    print(perimeter)