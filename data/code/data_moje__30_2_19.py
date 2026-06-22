import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    result = calculate_circle_area(5.0)
    print(result)