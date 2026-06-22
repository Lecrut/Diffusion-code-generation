def get_max_salary(salaries):
    if salaries is None:
        return 0
    valid_salaries = [s for s in salaries if s is not None and isinstance(s, (int, float))]
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_data_1 = [50000, 60000, None, 75000, None, 45000]
    sample_data_2 = []
    sample_data_3 = [None, None, None]
    sample_data_4 = None
    sample_data_5 = [30000, None, 25000, None]

    print(get_max_salary(sample_data_1))
    print(get_max_salary(sample_data_2))
    print(get_max_salary(sample_data_3))
    print(get_max_salary(sample_data_4))
    print(get_max_salary(sample_data_5))