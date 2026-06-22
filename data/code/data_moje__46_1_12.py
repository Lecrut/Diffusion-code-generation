def get_highest_salary(salaries):
    if not salaries:
        return None
    highest = salaries[0]
    for salary in salaries:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [50000, 85000, 42000, 98000, 63000]
    result = get_highest_salary(sample_salaries)
    print(result)