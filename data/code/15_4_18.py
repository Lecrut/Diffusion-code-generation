def get_penultimate(items):
    if len(items) < 2:
        return None
    return items[-2]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10],
        [],
        ['a', 'b'],
        [True, False, True]
    ]

    for case in test_cases:
        result = get_penultimate(case)
        print(result)