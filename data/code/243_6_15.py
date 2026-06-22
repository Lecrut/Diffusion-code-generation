import math

def calculate_circle_perimeter():
    radius = 100
    perimeter = 2 * math.pi * radius
    return float(perimeter)

if __name__ == '__main__':
    sample_radius = 50
    perimeter = calculate_circle_perimeter()
    print(f"Perimeter with radius {sample_radius}: {perimeter:.2f}")