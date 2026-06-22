import math

def calculate_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'small': 1, 'medium': 3, 'large': 5}
    for size, radius in sample_values.items():
        area = calculate_area(radius)
        print(f"The area of a {size} circle with radius {radius} is {area:.2f}")