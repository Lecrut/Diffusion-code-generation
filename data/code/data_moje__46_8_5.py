def find_max_salary(salary_entries):
    if salary_entries is None:
        return 0
    valid_salaries = []
    for entry in salary_entries:
        if entry is None:
            continue
        if isinstance(entry, (int, float)):
            valid_salaries.append(entry)
        elif isinstance(entry, str):
            try:
                valid_salaries.append(float(entry))
            except (ValueError, TypeError):
                continue
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_entries = [5000, None, 8000, "invalid", -100, 12000.5, [], {}, "7500"]
    result = find_max_salary(sample_entries)
    print(result)
    empty_result = find_max_salary([])
    print(empty_result)
    none_result = find_max_salary(None)
    print(none_result)
    all_invalid_result = find_max_salary([None, "abc", [], {}, []])
    print(all_invalid_result)