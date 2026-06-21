def get_middle_element(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    middle_index = len(sequence) // 2
    if len(sequence) % 2 == 1:
        return sequence[middle_index]
    else:
        return sequence[middle_index - 1]

if __name__ == '__main__':
    test_cases = [
        (list(range(1, 6)), 3),
        (list(range(1, 7)), 3),
        ("hello", "l"),
        ("worlds", "l"),
        ((10, 20, 30, 40, 50), 30),
        ((10, 20, 30, 40), 20),
        (["a", "b", "c", "d", "e"], "c"),
        (["x", "y", "z", "w"], "y"),
        (range(100, 101), 100),
        (range(100, 102), 100),
    ]
    for sequence, expected in test_cases:
        result = get_middle_element(sequence)
        print(f"Sequence: {sequence}, Middle: {result}, Expected: {expected}, Match: {result == expected}")
    try:
        get_middle_element([])
    except ValueError as e:
        print(f"Empty sequence error caught: {e}")