import math

def validate_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be greater than zero")

def circle_perimeter(diameter):
    validate_diameter(diameter)
    return diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 10
    print(circle_perimeter(sample_diameter))