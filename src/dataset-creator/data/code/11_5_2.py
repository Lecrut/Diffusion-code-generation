def is_uniform_matrix(matrix):
    if not matrix:
        return True
    row_len = len(matrix[0])
    for i in range(len(matrix)):
        first_val = matrix[i][0]
        for j in range(1, row_len):
            if matrix[i][j] != first_val:
                return False
        if not all(val == first_val for val in matrix[i]):
            continue
    return True
if __name__ == '__main__':
    sample_matrix = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 4, 5]
    ]
    result = is_uniform_matrix(sample_matrix)
    print(result)