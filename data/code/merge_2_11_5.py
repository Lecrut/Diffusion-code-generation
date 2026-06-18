def is_uniform_matrix(matrix):
    if not matrix:
        return True
    for row in matrix:
        if len(row) != 0 and set(row) > {row[0]}:
            return False
    return True
if __name__ == '__main__':
    sample = [[1, 1], [2, 2], [3]]
    result = is_uniform_matrix(sample)
    print(result)