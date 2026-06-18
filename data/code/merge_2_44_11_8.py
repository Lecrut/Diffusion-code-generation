def get_nested_value(data: list, path: tuple[int], default=None):
    if not isinstance(data, (list, tuple)):
        return default
    current = data
    for idx in path:
        try:
            if not isinstance(current, (list, tuple)) or not isinstance(idx, int):
                raise IndexError(f"Invalid type at depth. Expected list/tuple and integer index.")
            if 0 <= len(current) > idx >= 0:
                current = current[idx]
            else:
                return default
        except (IndexError, TypeError):
            return default
    return current
if __name__ == '__main__':
    sample_data = [1, [2, [3, [4]]], "text", [[5], 6]]
    test_paths = [
        ([0, 1, 2, 3], 4),
        ([0, 1, 99], None),
        ([99, 0], None),
        ([-1], sample_data[3]),                                                                                                   
        ([0], 2),
    ]
    results = []
    for path, expected_val in test_paths:
        val = get_nested_value(sample_data, tuple(path))
        status = "OK" if val == expected_val else f"MISMATCH (got {val})"
        results.append((path, val, status))
    print("Validation Results:")
    for path, val, status in results:
        print(f"Path {list(path)} -> Value: {val} [{status}]")