import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    test_radii = [5, 0, 10.5]
    for r in test_radii:
        try:
            area = calculate_circle_area(r)
            print(f"Radius: {r}, Area: {area}")
        except ValueError as e:
            print(f"Radius: {r}, Error: {e}")
    try:
        calculate_circle_area(-3)
    except ValueError as e:
        print(f"Radius: -3, Error: {e}")