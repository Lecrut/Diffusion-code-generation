SALARY_DATA = [
    45000,
    52000,
    60000,
    48000,
    75000,
    55000,
    62000,
]

def get_maximum_salary(data):
    return max(data)

if __name__ == '__main__':
    salaries = SALARY_DATA
    max_salary = get_maximum_salary(salaries)
    print(max_salary)