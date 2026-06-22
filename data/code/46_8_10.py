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
    sample_cases = [
        [5000, 6000, 7000],
        [],
        None,
        [None, 4000, None],
        [3000, None, 5000, "invalid", 2000],
        [None, None, None],
        [100.5, 200.75, 300.25]
    ]
    for case in sample_cases:
        result = get_max_salary(case)
        print(result)