def calculate_symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError('Both arguments must be sets.')
    sym_diff = set1 ^ set2
    return sym_diff
if __name__ == '__main__':
    try:
        set_x = {7, 8, 9, 10}
        set_y = {9, 10, 11, 12}
        result_xy = calculate_symmetric_difference(set_x, set_y)
        print('Symmetric difference of set_x and set_y:', result_xy)
    except ValueError as e:
        print(e)