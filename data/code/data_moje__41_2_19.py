def calculate_rhombus_area(diagonal_a, diagonal_b):
    if diagonal_a <= 0 or diagonal_b <= 0:
        raise ValueError("Diagonals must be positive numbers")
    return (diagonal_a * diagonal_b) / 2

if __name__ == '__main__':
    sample_diagonal_1 = 10
    sample_diagonal_2 = 14
    result = calculate_rhombus_area(sample_diagonal_1, sample_diagonal_2)
    print(result)