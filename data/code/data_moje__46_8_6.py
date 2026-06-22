def get_max_salary(salary_entries):
    valid_salaries = []
    for entry in salary_entries:
        if entry is None:
            continue
        if isinstance(entry, (int, float)) and entry >= 0:
            valid_salaries.append(entry)
    return max(valid_salaries) if valid_salaries else 0

if __name__ == '__main__':
    hardcoded_salaries = [5000, 6000, None, 7000, -1000, "invalid", 8000]
    result = get_max_salary(hardcoded_salaries)
    print(result)