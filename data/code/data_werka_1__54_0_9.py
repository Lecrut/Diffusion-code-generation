import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    SAMPLE_RADIUS_SMALL = 1
    SAMPLE_RADIUS_MEDIUM = 3
    SAMPLE_RADIUS_LARGE = 5
    areas = {'small': calculate_circle_area(SAMPLE_RADIUS_SMALL), 'medium': calculate_circle_area(SAMPLE_RADIUS_MEDIUM), 'large': calculate_circle_area(SAMPLE_RADIUS_LARGE)}
    for size, area in areas.items():
        print(f"The area of a circle with {size} radius ({eval(f'SAMPLE_RADIUS_{size.upper()}')}) is: {area}")