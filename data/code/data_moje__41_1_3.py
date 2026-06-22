def compute_rhombus_area(diagonal_a: float, diagonal_b: float) -> float:
    return 0.5 * diagonal_a * diagonal_b

if __name__ == '__main__':
    sample_diagonal_a: float = 10.0
    sample_diagonal_b: float = 8.0
    result: float = compute_rhombus_area(sample_diagonal_a, sample_diagonal_b)
    print(result)