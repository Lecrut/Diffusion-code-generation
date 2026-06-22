import math
PI = math.pi

def calculate_perimeter(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    sample_radius = 10
    perimeter = calculate_perimeter(sample_radius)
    print(f'Perimeter: {perimeter}')