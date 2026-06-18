def get_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty and has no final element.")
    return sequence[-1]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "List"),
        ("abc", "String"),
        ((5,), "Tuple"),
        ((), "Empty Tuple - Expected Exception"),
        ([], "Empty List - Expected Exception"),
        ("", "Empty String - Expected Exception")
    ]
    for seq, desc in test_cases:
        try:
            result = get_last_element(seq)
            print(f"{desc}: {result}")
        except ValueError as e:
            print(f"{desc} raised exception: {e}")