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
        [8, 3, 9]
    ]
    print(find_max_in_matrix(matrix1))
    matrix2 = [
        [10, 4, 7, 1],
        [2, 9, 3, 8],
        [5, 6, 11, 12]
    ]
    print(find_max_in_matrix(matrix2))
    matrix3 = [
        [-5, -10],
        [-2, -1]
    ]
    print(find_max_in_matrix(matrix3))
    matrix4 = [
        [42]
    ]
    print(find_max_in_matrix(matrix4))