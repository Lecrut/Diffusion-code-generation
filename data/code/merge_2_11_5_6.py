def is_uniform_matrix(matrix):
    if not matrix:
        return True
    first_row = set(matrix[0])
    for row in matrix:
        if len(set(row)) != 1:
            return False
        current_set = set(row)
        if current_set != first_row or (not first_row and len(current_set) > 1):
             return False
    return True
def check_matrix(matrix):
    if not matrix:
        return True
    first_row = set(map(str, matrix[0]))
    for row in matrix:
        current_set = set(map(str, row))
        if len(current_set) > 1 or not any(x == next(iter(first_row), None) for x in current_set):
            return False
    return True
def solve():
    matrix = [
        ['a', 'b'], 
        ['c', 'd']
    ]
    result = check_matrix(matrix)
    print(result)
if __name__ == '__main__':
    solve()