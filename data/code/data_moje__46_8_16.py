def get_max_salary(salaries):
    if not salaries:
        return 0
    valid_salaries = []
    for s in salaries:
        if s is not None:
            valid_salaries.append(s)
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_data = [None, 50000, 75000, None, 60000, 0, 80000]
    sample_data_empty = []
    sample_data_none_only = [None, None]
    print(get_max_salary(sample_data))
    print(get_max_salary(sample_data_empty))
    print(get_max_salary(sample_data_none_only))