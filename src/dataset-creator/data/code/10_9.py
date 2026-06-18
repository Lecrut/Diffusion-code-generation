def calculate_matrix_sum(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    return total_sum
if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    matrix2 = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
    matrix3 = [
        [1, 1, 1, 1],
        [2, 2, 2, 2]
    ]
    print(calculate_matrix_sum(matrix1))
    print(calculate_matrix_sum(matrix2))
    print(calculate_matrix_sum(matrix3))