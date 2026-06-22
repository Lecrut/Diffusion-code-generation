DIAGONAL_FACTORS = {'x': 0.5, 'y': 0.5}
compute_rhombus_area = lambda d1, d2: DIAGONAL_FACTORS['x'] * d1 * d2
if __name__ == '__main__':
    first_diagonal = 6.0
    second_diagonal = 8.0
    print(compute_rhombus_area(first_diagonal, second_diagonal))