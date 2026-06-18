def get_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    return sequence[-1]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "Expected last element"),
        ("hello", "Expected 'o'"),
        ((), "Empty tuple exception"),
        ([], "Empty list exception")
    ]
    for seq, desc in test_cases:
        try:
            result = get_last_element(seq)
            print(f"{desc}: {result}")
        except ValueError as e:
            print(f"{desc} raised error: {e}")