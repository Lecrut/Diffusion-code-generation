import math

def calculate_surface_area(dimensions: tuple) -> float:
    a, b, c = dimensions
    return 2.0 * (a * b + b * c + c * a)

if __name__ == '__main__':
    dims = (1.0, 2.0, 3.0)
    area = calculate_surface_area(dims)
    print(area)