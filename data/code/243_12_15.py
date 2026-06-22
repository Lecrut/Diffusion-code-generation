import math

def circle_perimeter(diameter):
    if diameter < 0:
        raise ValueError("Diameter must be non-negative.")
    return diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 15
    try:
        perimeter = circle_perimeter(sample_diameter)
        print(perimeter)
    except ValueError as e:
        print(e)