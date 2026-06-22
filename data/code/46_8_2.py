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
    sample_data = [50000, None, 75000.50, None, 60000, '', [], None]
    result = get_max_salary(sample_data)
    print(result)
    
    empty_data = []
    print(get_max_salary(empty_data))
    
    none_data = None
    print(get_max_salary(none_data))
    
    all_none_data = [None, None, None]
    print(get_max_salary(all_none_data))