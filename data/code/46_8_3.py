def get_max_salary(salaries):
    if salaries is None or len(salaries) == 0:
        return 0
    valid_salaries = []
    for item in salaries:
        if item is not None and isinstance(item, (int, float)):
            valid_salaries.append(item)
    if len(valid_salaries) == 0:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_data = [5000, None, 7500, None, 3000]
    sample_data_empty = []
    sample_data_none = None
    sample_data_invalid = [None, None, "error"]
    print(get_max_salary(sample_data))
    print(get_max_salary(sample_data_empty))
    print(get_max_salary(sample_data_none))
    print(get_max_salary(sample_data_invalid))