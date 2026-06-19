def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    sample_a = 3.0
    sample_b = 4.0
    sample_c = 5.0
    perimeter = calculate_triangle_perimeter(sample_a, sample_b, sample_c)
    print(perimeter)