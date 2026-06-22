def get_max_salary(salary_entries):
    if salary_entries is None:
        return 0
    valid_salaries = []
    for entry in salary_entries:
        if entry is not None and isinstance(entry, (int, float)):
            valid_salaries.append(entry)
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_salaries_1 = [5000, 6000, None, 7000, 'invalid', 3000]
    print(get_max_salary(sample_salaries_1))
    sample_salaries_2 = []
    print(get_max_salary(sample_salaries_2))
    sample_salaries_3 = None
    print(get_max_salary(sample_salaries_3))
    sample_salaries_4 = [None, None, 'not a number']
    print(get_max_salary(sample_salaries_4))
    sample_salaries_5 = [1000, 2000, 3000]
    print(get_max_salary(sample_salaries_5))