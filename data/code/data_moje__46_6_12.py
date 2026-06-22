SALARY_DATA = [
    50000,
    60000,
    75000,
    82000,
    90000,
    105000,
    110000,
    125000,
]

def get_maximum_salary(data):
    if not data:
        return None
    max_salary = data[0]
    for salary in data:
        if salary > max_salary:
            max_salary = salary
    return max_salary

if __name__ == '__main__':
    data = SALARY_DATA
    result = get_maximum_salary(data)
    print(result)