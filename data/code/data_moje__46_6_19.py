SALARY_DATA = [50000, 60000, 55000, 70000, 45000, 80000, 65000, 75000, 48000, 90000]

def get_maximum_salary(data):
    if not data:
        raise ValueError("Data list must not be empty")
    max_sal = data[0]
    for salary in data:
        if salary > max_sal:
            max_sal = salary
    return max_sal

if __name__ == '__main__':
    result = get_maximum_salary(SALARY_DATA)
    print(result)