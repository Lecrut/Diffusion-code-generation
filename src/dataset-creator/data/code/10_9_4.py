def sum_matrix(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total
if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(sum_matrix(matrix1))
    matrix2 = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
    print(sum_matrix(matrix2))
    matrix3 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print(sum_matrix(matrix3))