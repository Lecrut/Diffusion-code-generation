import math

def circle_perimeter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be greater than zero.")
    return diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 25
    print(circle_perimeter(sample_diameter))