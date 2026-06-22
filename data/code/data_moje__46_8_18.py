def get_max_salary(salary_entries):
    if salary_entries is None:
        return 0
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
    sample_salaries = [5000, None, 8000, "", 3000, -100, "invalid", None, 12000]
    result = get_max_salary(sample_salaries)
    print(result)
    
    empty_list = []
    result_empty = get_max_salary(empty_list)
    print(result_empty)
    
    none_input = None
    result_none = get_max_salary(none_input)
    print(result_none)
    
    all_none = [None, None, None]
    result_all_none = get_max_salary(all_none)
    print(result_all_none)
    
    negative_salaries = [-500, -1000, -200]
    result_negative = get_max_salary(negative_salaries)
    print(result_negative)
    
    mixed_invalid = [None, "", [], {}, "abc", -1, 0]
    result_mixed = get_max_salary(mixed_invalid)
    print(result_mixed)