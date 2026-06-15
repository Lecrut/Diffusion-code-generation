def find_max_in_matrix(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    max_element = matrix[0][0]
    for row in matrix:
        if row:
            row_max = max(row)
            if row_max > max_element:
                max_element = row_max
    return max_element
if __name__ == '__main__':
    matrix1 = [
        [1, 5, 2],
        [8, 3, 9],
        [4, 7, 6]
    ]
    print(find_max_in_matrix(matrix1))
    matrix2 = [
        [-10, -5, -20],
        [-30, -1, -15]
    ]
    print(find_max_in_matrix(matrix2))
    matrix3 = [
        [100]
    ]
    print(find_max_in_matrix(matrix3))
    matrix4 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(find_max_in_matrix(matrix4))