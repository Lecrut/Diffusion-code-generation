def get_nested_value(data: list | None, path: tuple[int], default=None):
    if not isinstance(path, tuple) or len(path) == 0:
        return default
    current = data
    for index in path:
        if not isinstance(current, (list, tuple)):
            return default
        try:
            idx = int(index)
            current = current[idx]
        except IndexError:
            return default
        except ValueError:
            return default
    return current
if __name__ == '__main__':
    sample_data = [10, 20, [30, 40, [[50], [60]]], "text"]
    result_1 = get_nested_value(sample_data, (2, 2, 1))
    result_2 = get_nested_value(sample_data, (0, 5))
    result_3 = get_nested_value(sample_data, (99, 1))
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")
    print(f"Result 3: {result_3}")