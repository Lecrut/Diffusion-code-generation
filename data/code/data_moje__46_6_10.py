SALARY_DATA = [
    50000.0,
    65000.0,
    72000.0,
    85000.0,
    92000.0,
    110000.0,
    125000.0,
    150000.0,
]

def get_maximum_salary(salaries: list) -> float:
    return max(salaries)

if __name__ == '__main__':
    result = get_maximum_salary(SALARY_DATA)
    print(result)