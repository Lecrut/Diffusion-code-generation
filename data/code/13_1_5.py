def resolve_index(matrix, target_row, target_col, default_value):
    row_count = len(matrix)
    if target_row < 0 or target_row >= row_count:
        return default_value
    current_row = matrix[target_row]
    if not isinstance(current_row, (list, tuple)):
        return default_value
    col_count = len(current_row)
    if target_col < 0 or target_col >= col_count:
        return default_value
    return current_row[target_col]

if __name__ == '__main__':
    grid = [
        [100, 200, 300],
        [400, 500, 600],
        [700, 800, 900]
    ]
    valid_result = resolve_index(grid, 1, 1, -999)
    print(valid_result)
    out_of_bounds_row = resolve_index(grid, 10, 1, -999)
    print(out_of_bounds_row)
    out_of_bounds_col = resolve_index(grid, 0, 10, -999)
    print(out_of_bounds_col)
    jagged_grid = [
        [1],
        [2, 2],
        [3, 3, 3]
    ]
    jagged_result = resolve_index(jagged_grid, 1, 5, "MISSING")
    print(jagged_result)