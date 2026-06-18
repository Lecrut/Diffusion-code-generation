def is_uniform_matrix(matrix):
    if not matrix:
        return True
    first_row = set()
    for row in matrix:
        current_set = set(row)
        if len(current_set) > 1 or (not isinstance(first_row, int)) and current_set != first_row:
            return False
        if len(current_set) == 0:
            continue
        first_row = current_set
    return True
if __name__ == '__main__':
    sample_matrix_1 = [[1, 1], [2, 2]]
    sample_matrix_2 = [[1, 1], [3, 4]]
    result_1 = is_uniform_matrix(sample_matrix_1)
    result_2 = is_uniform_matrix(sample_matrix_2)
    print(result_1 and not result_2)