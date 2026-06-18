def get_first_element(data):
    if data is None:
        raise ValueError("Input cannot be null")
    try:
        return next(iter(data))
    except StopIteration:
        raise IndexError("The provided collection is empty")
if __name__ == '__main__':
    test_cases = [None, [], [1], "a", {}, {"key": "val"}]
    for i, data in enumerate(test_cases):
        try:
            result = get_first_element(data)
            print(f"Test case {i}: Success - First element is '{result}'")
        except (ValueError, IndexError) as e:
            print(f"Test case {i}: Error - {e}")