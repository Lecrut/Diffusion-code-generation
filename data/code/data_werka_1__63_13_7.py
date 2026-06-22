def fetch_first_element(sequence):
    try:
        return sequence[0]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    test_cases = [
        [100, 200, 300],
        (400, 500, 600),
        [],
        (),
        "world",
        None,
        789
    ]
    for case in test_cases:
        print(fetch_first_element(case))