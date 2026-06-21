import math

def area_of_circle(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 5.0
    result = area_of_circle(sample_radius)
    print(result)