def get_first_element(data):
    if data is None:
        raise ValueError("Input cannot be null.")
    try:
        return list(data)[0]
    except IndexError:
        raise ValueError("Collection is empty; no element to retrieve.")
if __name__ == '__main__':
    test_cases = [None, [], [1], "hello", {"a": 1}]
    for case in test_cases:
        try:
            result = get_first_element(case)
            print(f"Input: {case} -> Output: {result}")
        except ValueError as e:
            print(f"Error processing input {case}: {e}")