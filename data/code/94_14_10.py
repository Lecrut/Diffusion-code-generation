def any_true(sequence):
    return any(sequence)

if __name__ == '__main__':
    test_cases = [
        ([False, False], False),
        ([True, False], True),
        ([False, True], True),
        ([True, True], True),
        ([], False)
    ]
    
    for seq, expected in test_cases:
        result = any_true(seq)
        print(f"Sequence: {seq} -> Expected: {expected}, Result: {result}")