def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All sides must be numbers.")
    if any(x <= 0 for x in [a, b, c]):
        raise ValueError("All sides must be positive.")
    return a + b + c

if __name__ == '__main__':
    try:
        sample_a = 3.5
        sample_b = 4.2
        sample_c = 5.1
        perimeter = calculate_triangle_perimeter(sample_a, sample_b, sample_c)
        print(perimeter)
    except ValueError as e:
        print(e)