def find_max_salary(salary_entries):
    valid_salaries = []
    for entry in salary_entries:
        if entry is None:
            continue
        if isinstance(entry, (int, float)):
            if entry >= 0:
                valid_salaries.append(entry)
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_entries = [5000, None, -100, 7500, "", [1, 2], 3000, None, 0]
    result = find_max_salary(sample_entries)
    print(result)
    empty_entries = []
    result_empty = find_max_salary(empty_entries)
    print(result_empty)
    none_entries = [None, None, None]
    result_none = find_max_salary(none_entries)
    print(result_none)
    invalid_entries = ["a", "b", None, [], {}]
    result_invalid = find_max_salary(invalid_entries)
    print(result_invalid)