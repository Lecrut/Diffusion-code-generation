def find_midpoint_index(data):
    if not hasattr(data, '__len__') or isinstance(data, str) or type(data).__name__ in ('dict', 'set'):
        raise TypeError("Input must support length and integer indexing; strings, dicts, sets excluded.")
    try:
        n = len(data)
    except Exception as e:
        raise ValueError(f"Unable to determine sequence length. {e}") from None
    if n < 0 or not isinstance(n, int):
        raise ValueError("Length must be a non-negative integer.")
    mid_index = n // 2
    if n % 2 == 0:
        return None
    return mid_index
if __name__ == '__main__':
    test_cases = [
        ([1, 2], "Even length list"),
        ([5], "Odd length single item"),
        (range(3), "Range object odd"),
        ((-10,), "Negative value inside valid structure"),                                                                                                      
        ("", "Empty string treated as invalid type per docstring exclusion of strings"),
    ]
    for data, description in test_cases:
        try:
            result = find_midpoint_index(data)
            print(f"{description}: {result}")
        except (ValueError, TypeError) as e:
            print(f"{description} -> Error: {e}")