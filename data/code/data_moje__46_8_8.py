def get_max_salary(salary_list):
    valid_salaries = []
    if salary_list is None:
        return 0
    for item in salary_list:
        if item is None:
            continue
        if isinstance(item, (int, float)):
            valid_salaries.append(item)
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    test_data = [50000, None, 60000, 75000, None, 80000]
    result = get_max_salary(test_data)
    print(result)