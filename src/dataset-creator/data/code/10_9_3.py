def calculate_matrix_sum(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total
if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    result1 = calculate_matrix_sum(matrix1)
    print(result1)
    matrix2 = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
    result2 = calculate_matrix_sum(matrix2)
    print(result2)
    matrix3 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    result3 = calculate_matrix_sum(matrix3)
    print(result3)