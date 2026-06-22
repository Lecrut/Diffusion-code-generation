def get_max_salary(salaries):
    if not salaries:
        return 0
    valid_salaries = [s for s in salaries if s is not None and isinstance(s, (int, float))]
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    test_data = [50000, None, 75000, 0, None, 82000]
    result = get_max_salary(test_data)
    print(result)
    empty_data = []
    print(get_max_salary(empty_data))
    none_data = [None, None, None]
    print(get_max_salary(none_data))