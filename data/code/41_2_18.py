def calculate_rhombus_area(diagonal_1, diagonal_2):
    if diagonal_1 <= 0 or diagonal_2 <= 0:
        raise ValueError("Diagonals must be positive numbers")
    return 0.5 * diagonal_1 * diagonal_2

if __name__ == '__main__':
    sample_diagonal_1 = 10.0
    sample_diagonal_2 = 6.0
    result = calculate_rhombus_area(sample_diagonal_1, sample_diagonal_2)
    print(result)