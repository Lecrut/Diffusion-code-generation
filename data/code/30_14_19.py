import math

def get_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

if __name__ == "__main__":
    test_values = [0, 3, 10.0, 25.5]
    for val in test_values:
        print(get_circle_area(val))