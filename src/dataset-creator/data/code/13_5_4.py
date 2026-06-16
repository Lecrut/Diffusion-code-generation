def safe_max(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    try:
        return max(values)
    except ValueError as e:
        if "uncomparable types" in str(e).lower():
            raise TypeError(f"Mixed uncomparable types found in sequence. Valid values provided: {values}") from None
        else:
            raise
if __name__ == '__main__':
    test_cases = [
        [],
        [1, 2, 3],
        (4, 5),
        ["a", "b"],
        [1.0, 2.0]
    ]
    for i, data in enumerate(test_cases):
        try:
            result = safe_max(data)
            print(f"Test case {i}: Input={data}, Max Value={result}")
        except Exception as ex:
            print(f"Test case {i}: Error - {ex}")