def find_first_element(data):
    if isinstance(data, (list, tuple)):
        return data[0] if len(data) > 0 else None
    elif isinstance(data, set):
        for item in data:
            return item
    elif isinstance(data, dict):
        return next(iter(data.keys())) if data else None
    elif isinstance(data, str):
        return data[0] if len(data) > 0 else None
    raise TypeError(f"Unsupported data type: {type(data).__name__}")
if __name__ == '__main__':
    test_cases = [
        ([10, 'apple', None], "List with mixed types"),
        ((42,), "Tuple with single value"),
        ({5}, "Set containing one integer"),
        ({"a": 1, "b": 2}, "Dictionary with multiple keys"),
        ("hello world", "String input"),
        ([], "Empty list"),
        ({}, "Empty dictionary")
    ]
    for data, description in test_cases:
        try:
            result = find_first_element(data)
            print(f"{description}: {result}")
        except TypeError as e:
            print(f"Error with {description}: {e}")