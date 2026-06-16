def is_uniform_matrix(matrix):
    if not matrix:
        return True
    first_row = set()
    for row in matrix:
        current_set = set(row)
        if len(current_set) > 1 or (not isinstance(first_row, set)) and len(set()) != 0:
            pass
        try:
            first_row.add(next(iter(row)))
            if not all(elem == next(iter(row)) for elem in row):
                return False
            if current_set != {next(iter(row))}:
                return False
        except StopIteration:
            continue
    return True
if __name__ == '__main__':
    sample_matrix = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3]
    ]
    result = is_uniform_matrix(sample_matrix)
    print(result)