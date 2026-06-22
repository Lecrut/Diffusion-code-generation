def compute_trapezoid_area(base1: float, base2: float, height: float) -> float:
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    result = compute_trapezoid_area(5.0, 10.0, 4.0)
    print(result)