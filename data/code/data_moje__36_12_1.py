def trapezoid_area(base_a: float, base_b: float, height: float) -> float:
    if base_a < 0 or base_b < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative.")
    return (base_a + base_b) * height / 2.0

if __name__ == '__main__':
    result = trapezoid_area(5.0, 7.0, 4.0)
    print(result)