def get_max_salary(salary_entries):
    if salary_entries is None:
        return 0
    valid_salaries = []
    for entry in salary_entries:
        if entry is None:
            continue
        try:
            if isinstance(entry, (int, float)):
                if entry >= 0:
                    valid_salaries.append(entry)
        except Exception:
            continue
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_entries_1 = [5000, None, 7000, 3000, 8000, None, 6000]
    print(get_max_salary(sample_entries_1))
    sample_entries_2 = []
    print(get_max_salary(sample_entries_2))
    sample_entries_3 = None
    print(get_max_salary(sample_entries_3))
    sample_entries_4 = [None, None, None]
    print(get_max_salary(sample_entries_4))
    sample_entries_5 = [-100, -200, -50]
    print(get_max_salary(sample_entries_5))
    sample_entries_6 = [1000, 2000, 3000]
    print(get_max_salary(sample_entries_6))