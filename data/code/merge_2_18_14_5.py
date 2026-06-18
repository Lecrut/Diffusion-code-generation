def reverse_sequence(seq):
    if isinstance(seq, str):
        return seq[::-1]
    elif hasattr(seq, '__reversed__'):
        return list(reversed(seq))
    else:
        raise TypeError("Unsupported sequence type")
if __name__ == '__main__':
    test_cases = [
        ["apple", "banana"],
        "",
        [],
        12345,
        (6, 7),
    ]
    for case in test_cases:
        try:
            result = reverse_sequence(case)
            print(f"Input: {case} -> Output: {result}")
        except TypeError as e:
            print(f"Error with input {case}: {e}")