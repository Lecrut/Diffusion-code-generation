def get_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty and has no final element.")
    return sequence[-1]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "integers"),
        (["a", "b"], "strings"),
        ((5,), "single item tuple"),
        ([], "empty list")
    ]
    for seq, desc in test_cases:
        try:
            result = get_last_element(seq)
            print(f"{desc}: {result}")
        except ValueError as e:
            print(f"Error with {desc} ({e})")