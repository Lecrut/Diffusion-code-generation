def get_first_element(items):
    if items is None:
        raise TypeError("Input cannot be null.")
    if not isinstance(items, list):
        raise ValueError(f"Expected a list, got {type(items).__name__}.")
    if len(items) == 0:
        return None
    return items[0]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "Valid non-empty list"),
        (None, "Null input"),
        ([] , "Empty list"),
        ("abc", "Non-list string input"),
        ({}, "Empty dictionary passed as list")
    ]
    for data, description in test_cases:
        try:
            result = get_first_element(data)
            print(f"Test Case '{description}': Result is {result}")
        except (TypeError, ValueError) as e:
            print(f"Test Case '{description}': Error raised - {e.__class__.__name__}: {str(e)}")