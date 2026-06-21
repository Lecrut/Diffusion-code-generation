import math

def compute_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    r_sample = 7
    area_result = compute_circle_area(r_sample)
    print(area_result)