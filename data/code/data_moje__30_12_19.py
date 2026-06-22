import math

def compute_circle_area(radius: float) -> float:
    if radius < 0:
        return 0.0
    return math.pi * (radius * radius)

if __name__ == '__main__':
    result = compute_circle_area(7)
    print(result)
    result_zero = compute_circle_area(0)
    print(result_zero)
    result_neg = compute_circle_area(-5)
    print(result_neg)