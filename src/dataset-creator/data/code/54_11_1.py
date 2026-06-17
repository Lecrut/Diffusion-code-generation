def get_center_index(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be an iterable sequence like list or tuple.")
    length = len(sequence)
    return length // 2
if __name__ == '__main__':
    test_cases = [
        ([10], 0),
        ([1, 2, 3], 1),
        ([1, 2, 3, 4], 2),
        ((), -1),
        ("ab", 1)
    ]
    for seq in test_cases:
        try:
            result = get_center_index(seq[0]) if isinstance(seq, tuple) else get_center_index(list(seq))
            print(f"Center index of {seq}: {result}")
        except Exception as e:
            print(f"Error with input {e.args[1] if len(e.args) > 1 else str(e)}")