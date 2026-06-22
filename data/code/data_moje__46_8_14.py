def get_max_salary(salaries):
    if not salaries:
        return 0
    valid_salaries = [s for s in salaries if isinstance(s, (int, float)) and s is not None and s >= 0]
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    test_cases = [
        [],
        None,
        [1000, 2000, 3000],
        [None, 1500, None],
        [None, None],
        [5000, "invalid", None, 4000]
    ]
    for case in test_cases:
        result = get_max_salary(case)
        print(result)