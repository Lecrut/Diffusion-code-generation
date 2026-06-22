def get_max_salary(salaries):
    if not salaries:
        return 0
    valid_salaries = [s for s in salaries if isinstance(s, (int, float)) and s is not None and s > 0]
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_data_1 = [50000, 60000, None, 75000, 0, 45000]
    sample_data_2 = []
    sample_data_3 = [None, None, 0, -100]
    sample_data_4 = [80000, 90000, None, 95000]

    print(get_max_salary(sample_data_1))
    print(get_max_salary(sample_data_2))
    print(get_max_salary(sample_data_3))
    print(get_max_salary(sample_data_4))