def find_first_element(data):
    if isinstance(data, (list, tuple)):
        return data[0] if len(data) > 0 else None
    elif isinstance(data, set):
        try:
            iterator = iter(data)
            return next(iterator)
        except StopIteration:
            return None
    elif isinstance(data, dict):
        if len(data) > 0:
            for key in data.keys():
                return data[key]
    elif isinstance(data, str):
        return data[0] if len(data) > 0 else None
    raise TypeError(f"Unsupported data type provided. Expected list, tuple, set, dict, or string.")
if __name__ == '__main__':
    test_cases = [
        ([10, 'a', True], "List with mixed types"),
        ((5,), "Single element tuple"),
        ({'key': 'value'}, "Dictionary example"),
        ("Python", "String input"),
        (set(), "Empty set"),
        ([], "Empty list")
    ]
    for data, description in test_cases:
        try:
            result = find_first_element(data)
            print(f"{description}: {result}")
        except Exception as e:
            print(f"Error processing {data} ({type(data).__name__}): {e}")