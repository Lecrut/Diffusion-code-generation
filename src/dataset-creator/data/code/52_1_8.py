def safe_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty and cannot return a final element.")
    return sequence[-1]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "integers"),
        (['a', 'b'], "strings"),
        ((5.0,), "floats"),
        ([], "empty list"),
    ]
    for data, desc in test_cases:
        try:
            result = safe_last_element(data)
            print(f"{desc}: {result}")
        except ValueError as e:
            print(f"{desc} raised exception: {e}")