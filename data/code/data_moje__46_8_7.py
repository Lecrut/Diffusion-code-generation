def get_max_salary(salaries):
    if not salaries:
        return 0
    valid_salaries = [s for s in salaries if s is not None and isinstance(s, (int, float)) and s >= 0]
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    test_cases = [
        [],
        None,
        [100, 200, 300],
        [None, 150, None],
        [None, None],
        [500, 0, 250],
        [None]
    ]
    for case in test_cases:
        result = get_max_salary(case)
        print(result)