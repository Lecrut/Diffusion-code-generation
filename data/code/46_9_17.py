def find_max_salary(salary_data):
    max_sal = float('-inf')
    for dept in salary_data:
        for salary in dept:
            if salary > max_sal:
                max_sal = salary
    return max_sal

if __name__ == '__main__':
    sample_data = [
        [50000, 60000, 55000],
        [70000, 80000, 75000],
        [45000, 50000, 52000]
    ]
    result = find_max_salary(sample_data)
    print(result)