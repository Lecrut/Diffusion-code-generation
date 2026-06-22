import math

def calculate_circle_area(radius: float) -> float:
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius_value = 5.0
    result = calculate_circle_area(radius_value)
    print(result)