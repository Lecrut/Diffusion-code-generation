def calculate_trapezoid_area(base_a, base_b, height):
    if base_a < 0 or base_b < 0 or height < 0:
        raise ValueError("Base lengths and height must be non-negative.")
    return (base_a + base_b) * height / 2

if __name__ == "__main__":
    result_1 = calculate_trapezoid_area(5, 10, 7)
    result_2 = calculate_trapezoid_area(3.5, 4.5, 2)
    print(result_1)
    print(result_2)