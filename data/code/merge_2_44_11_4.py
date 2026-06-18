def get_nested_value(data: list, path: tuple[int], default=None):
    current = data
    for index in path:
        if not isinstance(current, (list, tuple)):
            return default
        try:
            next_item = current[index]
        except IndexError:
            return default
        current = next_item
    return current
if __name__ == '__main__':
    sample_data = [10, 20, [30, 40], [[50, 60], [70]]]
    path_1: tuple[int] = (2, 0)
    result_1 = get_nested_value(sample_data, path_1)
    path_2: tuple[int] = (3, 1, 0)
    result_2 = get_nested_value(sample_data, path_2)
    path_3: tuple[int] = (9,)
    result_3 = get_nested_value(sample_data, path_3)
    print(result_1)             
    print(result_2)             
    print(result_3)