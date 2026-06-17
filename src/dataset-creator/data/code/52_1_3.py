def get_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty and has no final element.")
    return sequence[-1]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "List"),
        ("hello", "String"),
        ((4,), "Tuple with one item"),
        ((), "Empty tuple - should raise error"),
        ([], "Empty list - should raise error")
    ]
    for seq, desc in test_cases:
        print(f"Testing {desc}: Input = {seq}")
        try:
            result = get_last_element(seq)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error raised (expected): {e}")