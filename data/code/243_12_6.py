import math

def compute_circle_perimeter(diameter):
    return diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 12
    perimeter_result = compute_circle_perimeter(sample_diameter)
    print(perimeter_result)