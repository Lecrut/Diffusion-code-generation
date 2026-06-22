def get_max_salary(salary_entries):
    if salary_entries is None:
        return 0
    valid_salaries = []
    for entry in salary_entries:
        if isinstance(entry, (int, float)) and not isinstance(entry, bool):
            valid_salaries.append(entry)
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    salaries1 = [50000, 60000, 75000, None, 80000]
    print(get_max_salary(salaries1))

    salaries2 = None
    print(get_max_salary(salaries2))

    salaries3 = []
    print(get_max_salary(salaries3))

    salaries4 = [None, None, 'invalid']
    print(get_max_salary(salaries4))