def get_first_element(sequence):
    try:
        return sequence[0]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    test_cases = [
        [10, 20, 30],
        (40, 50, 60),
        [],
        (),
        "hello",
        None,
        123
    ]
    for case in test_cases:
        print(get_first_element(case))