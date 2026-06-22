SALARIES = [50000, 60000, 75000, 55000, 80000, 95000, 65000, 70000]

def get_max_salary(salary_list):
    if not salary_list:
        raise ValueError("Salary list cannot be empty")
    max_sal = salary_list[0]
    for sal in salary_list[1:]:
        if sal > max_sal:
            max_sal = sal
    return max_sal

if __name__ == '__main__':
    result = get_max_salary(SALARIES)
    print(result)