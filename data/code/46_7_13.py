def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    sample_a = 7.5
    sample_b = 8.2
    sample_c = 9.3
    perimeter = calculate_triangle_perimeter(sample_a, sample_b, sample_c)
    print(perimeter)