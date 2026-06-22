def get_middle_element(seq):
    if len(seq) == 0:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(seq) // 2
    return seq[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        "hello",
        ("a", "b", "c", "d", "e"),
        [100],
        range(1, 6)
    ]
    for case in test_cases:
        print(get_middle_element(case))
    try:
        get_middle_element([])
    except ValueError as e:
        print(e)