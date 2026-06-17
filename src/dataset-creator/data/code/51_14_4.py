def get_first_element(data):
    if data is None:
        raise ValueError("Input cannot be null.")
    try:
        return list(data)[0]
    except IndexError:
        raise IndexError("Collection is empty; no element to retrieve.")
if __name__ == '__main__':
    test_cases = [None, [], [1], "hello", {"key": 42}]
    for item in test_cases:
        try:
            result = get_first_element(item)
            print(f"Input: {item} -> Output: {result}")
        except (ValueError, IndexError) as e:
            print(f"Input: {item} -> Error: {e}")