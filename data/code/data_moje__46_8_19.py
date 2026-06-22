def get_max_salary(salary_list):
    if salary_list is None:
        return 0
    valid_salaries = []
    for entry in salary_list:
        if entry is not None and isinstance(entry, (int, float)) and entry >= 0:
            valid_salaries.append(entry)
    if not valid_salaries:
        return 0
    max_value = valid_salaries[0]
    for i in range(1, len(valid_salaries)):
        if valid_salaries[i] > max_value:
            max_value = valid_salaries[i]
    return max_value

if __name__ == '__main__':
    sample_data = [None, 50000, 0, 75000, None, 60000, -100]
    empty_list = []
    none_list = None
    result1 = get_max_salary(sample_data)
    result2 = get_max_salary(empty_list)
    result3 = get_max_salary(none_list)
    print(result1)
    print(result2)
    print(result3)