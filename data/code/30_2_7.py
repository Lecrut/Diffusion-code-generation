import math

def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == '__main__':
    print(calculate_circle_area(5.0))