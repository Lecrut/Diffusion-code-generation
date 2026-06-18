def get_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty and has no final element.")
    return sequence[-1]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "List"),
        ("hello", "String"),
        ((4, 5), "Tuple"),
        (["a"], "Single item list"),
        ([], "Empty list")
    ]
    for data, desc in test_cases:
        try:
            result = get_last_element(data)
            print(f"{desc}: {result}")
        except ValueError as e:
            print(f"{desc} raised exception: {e}")