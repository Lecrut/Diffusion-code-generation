def get_2d_element(data, row, col, default=None):
    if not isinstance(data, list):
        return default
    if row < 0 or row >= len(data):
        return default
    inner_list = data[row]
    if not isinstance(inner_list, list):
        return default
    if col < 0 or col >= len(inner_list):
        return default
    return inner_list[col]

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = get_2d_element(matrix, 1, 1)
    print(result)
    result_out = get_2d_element(matrix, 5, 5, "Fallback")
    print(result_out)