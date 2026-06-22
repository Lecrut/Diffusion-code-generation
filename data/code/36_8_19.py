def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    result = calculate_trapezoid_area(5.0, 7.0, 4.0)
    print(result)