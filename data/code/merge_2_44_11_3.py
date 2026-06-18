def get_nested_value(data: list, path: tuple[int], default=None):
    current = data
    for idx in path:
        if not isinstance(current, (list, tuple)):
            return default
        try:
            next_item = current[idx]
            if isinstance(next_item, (list, tuple)) and len(path) > 1:
                current = next_item
            else:
                break
        except IndexError:
            return default
    return current
if __name__ == '__main__':
    sample_data = [
        ["a", "b"],
        [["c", "d"], ["e"]]
    ]
    result_1 = get_nested_value(sample_data, (0, 1))
    print(result_1)
    result_2 = get_nested_value(sample_data, (5, 0), "Not Found")
    print(result_2)