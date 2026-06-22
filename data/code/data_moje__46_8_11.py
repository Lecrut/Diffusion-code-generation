def find_max_salary(salary_entries):
    valid_salaries = []
    for entry in salary_entries:
        if entry is not None:
            try:
                salary_value = float(entry)
                valid_salaries.append(salary_value)
            except (ValueError, TypeError):
                continue
    if valid_salaries:
        return max(valid_salaries)
    return 0.0

if __name__ == '__main__':
    sample_entries = [5000, None, 7500, "", 12000, "invalid", None, 3000]
    result = find_max_salary(sample_entries)
    print(result)

    empty_entries = []
    result_empty = find_max_salary(empty_entries)
    print(result_empty)

    none_entries = [None, None, None]
    result_none = find_max_salary(none_entries)
    print(result_none)