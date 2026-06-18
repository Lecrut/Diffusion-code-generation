def safe_max(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    try:
        return max(set(sequence), key=sequence.count)
    except TypeError as e:
        raise TypeError(f"Cannot compare mixed types in list. Original error: {e}")
if __name__ == '__main__':
    test_cases = [
        [],
        [1, 2, 3],
        ['a', 'b', 'c'],
        [1, 2, "three", None]
    ]
    for i, seq in enumerate(test_cases):
        try:
            result = safe_max(seq)
            print(f"Test case {i}: Max value is {result}")
        except Exception as e:
            print(f"Test case {i} failed with error: {e}")