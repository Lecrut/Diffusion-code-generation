def find_max_in_matrix(matrix):
    if not matrix:
        raise ValueError("Input matrix cannot be empty")
    max_element = matrix[0][0]
    for row in matrix:
        if row:
            current_row_max = max(row)
            if current_row_max > max_element:
                max_element = current_row_max
    return max_element
if __name__ == '__main__':
    matrix1 = [
        [1, 5, 2],
        [8, 3, 9],
        [4, 7, 6]
    ]
    print(find_max_in_matrix(matrix1))
    matrix2 = [
        [-10, -5],
        [-20, -1]
    ]
    print(find_max_in_matrix(matrix2))
    matrix3 = [
        [100, 50, 25],
        [10, 20, 30]
    ]
    print(find_max_in_matrix(matrix3))
    matrix4 = [[-5]]
    print(find_max_in_matrix(matrix4))