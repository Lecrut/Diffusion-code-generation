def get_first_element(data):
    if data is None:
        raise ValueError("Input cannot be null.")
    try:
        return list(data)[0]
    except IndexError:
        raise IndexError("The provided collection is empty.")
if __name__ == '__main__':
    test_cases = [
        (None, "Null input"),
        ([], "Empty list"),
        ([1, 2, 3], "Normal case"),
        ("abc", "String iterable"),
    ]
    for data, description in test_cases:
        try:
            result = get_first_element(data)
            print(f"{description}: {result}")
        except (ValueError, IndexError) as e:
            print(f"{description} raised an error: {e}")