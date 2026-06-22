def find_max_salary(salary_strings):
    try:
        return max(float(s) for s in salary_strings)
    except (ValueError, TypeError, StopIteration):
        return None

if __name__ == '__main__':
    salaries = ["50000.00", "75000.50", "120000.75", "30000.25", "95000.00", "invalid", "85000.00"]
    result = find_max_salary(salaries)
    print(result)