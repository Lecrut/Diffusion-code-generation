def find_max_in_matrix(matrix):
    if not matrix:
        raise ValueError("Matrix cannot be empty")
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
        [8, 3, 9]
    ]
    print(find_max_in_matrix(matrix1))
    matrix2 = [
        [10, 20, 5],
        [1, 15, 3]
    ]
    print(find_max_in_matrix(matrix2))
    matrix3 = [
        [-5, -1, -10],
        [-20, -3, -50]
    ]
    print(find_max_in_matrix(matrix3))
    matrix4 = [
        [100]
    ]
    print(find_max_in_matrix(matrix4))
    matrix5 = []
    try:
        print(find_max_in_matrix(matrix5))
    except ValueError as e:
        print(e)