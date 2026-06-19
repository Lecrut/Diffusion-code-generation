import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_values = [1, 2, 0, 10, 5.5]
    for radius in sample_values:
        area = calculate_circle_area(radius)
        print(f'Radius: {radius}, Area: {area}')