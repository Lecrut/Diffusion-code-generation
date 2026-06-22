SALARY_DATA = [
    50000,
    60000,
    75000,
    80000,
    95000,
    110000,
    125000,
]

def get_max_salary(salary_list):
    if not salary_list:
        return 0
    max_sal = salary_list[0]
    for sal in salary_list:
        if sal > max_sal:
            max_sal = sal
    return max_sal

if __name__ == '__main__':
    data = [45000, 52000, 61000, 58000, 70000]
    result = get_max_salary(data)
    print(result)