def count_elements(data):
    if not isinstance(data, list):
        raise TypeError(f"Expected 'list', got '{type(data).__name__}'")
    return len(data)
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "Valid integer list"),
        (["a", "b"], "Valid string list"),
        ([True, False], "Boolean values"),
        ("string", "Non-list input - should raise error"),
        (42, "Integer instead of list"),
    ]
    for data, description in test_cases:
        try:
            result = count_elements(data)
            print(f"Input: {data} ({description}) -> Count: {result}")
        except TypeError as e:
            print(f"Error with input '{type(data).__name__}': {e}")