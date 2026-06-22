SALARY_DATA = [50000, 62000, 75000, 48000, 91000, 67000, 55000, 83000]

def get_max_salary(salaries):
    if not salaries:
        return 0
    max_val = salaries[0]
    for value in salaries[1:]:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == "__main__":
    result = get_max_salary(SALARY_DATA)
    print(result)