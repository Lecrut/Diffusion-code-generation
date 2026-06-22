def get_max_salary(salaries):
    if salaries is None:
        return 0
    valid_salaries = [s for s in salaries if s is not None and isinstance(s, (int, float)) and s >= 0]
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    sample_data = [50000, None, 60000, 0, -10, 75000, 55000]
    result = get_max_salary(sample_data)
    print(result)
    print(get_max_salary(None))
    print(get_max_salary([]))
    print(get_max_salary([None, None, None]))
    print(get_max_salary([-5, -10]))