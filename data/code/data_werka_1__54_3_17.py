import math
PI = math.pi

def get_area(radius: float) -> float:
    return PI * radius ** 2
if __name__ == '__main__':
    radii = [5.0, 0.5, 10.5]
    for radius in radii:
        area = get_area(radius)
        print(f'The area for radius {radius} is {area}')