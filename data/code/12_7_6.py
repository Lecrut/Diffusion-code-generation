def get_middle_element(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 1:
        return sequence[mid_index]
    else:
        return sequence[mid_index - 1]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        "hello",
        ("a", "b", "c", "d", "e"),
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [100, 200],
        [5]
    ]
    
    for case in test_cases:
        result = get_middle_element(case)
        print(f"Input: {case}, Middle Element: {result}")