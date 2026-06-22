SALARY_DATA = [50000, 75000, 60000, 90000, 45000, 85000, 55000]

def get_max_salary(data):
    if not data:
        return None
    current_max = data[0]
    for salary in data:
        if salary > current_max:
            current_max = salary
    return current_max

if __name__ == '__main__':
    result = get_max_salary(SALARY_DATA)
    print(result)