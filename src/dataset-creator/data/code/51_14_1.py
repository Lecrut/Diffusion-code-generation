def get_first_element(data):
    if data is None:
        raise ValueError("Input cannot be null.")
    if not isinstance(data, list):
        raise TypeError(f"Expected a list, got {type(data).__name__}.")
    if len(data) == 0:
        return "Collection is empty."
    try:
        first_item = data[0]
        if isinstance(first_item, type(None)):
            raise ValueError("The collection contains no non-null elements.")
        return first_item
    except IndexError as e:
        raise RuntimeError(f"Failed to retrieve element from empty or invalid sequence: {str(e)}")
if __name__ == '__main__':
    test_cases = [
        ["apple", "banana"],
        [],
        None,
        {"key": "value"},                  
        [[1], []]                                                                      
    ]
    for i, case in enumerate(test_cases):
        try:
            result = get_first_element(case)
            print(f"Test Case {i + 1}: Input={case} -> Output={result}")
        except Exception as e:
            print(f"Test Case {i + 1}: Input={case} -> Error: {e.__class__.__name__}: {e}")