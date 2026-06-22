def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [a, b, c]):
        raise ValueError("All sides must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    sample_a = 7.2
    sample_b = 9.3
    sample_c = 11.4
    try:
        perimeter = calculate_triangle_perimeter(sample_a, sample_b, sample_c)
        print(perimeter)
    except ValueError as e:
        print(e)