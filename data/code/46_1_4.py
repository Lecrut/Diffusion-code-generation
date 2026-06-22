def get_highest_salary(salaries):
    if not salaries:
        return None
    highest = salaries[0]
    for salary in salaries:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [5000, 12000, 7500, 9000, 15000]
    result = get_highest_salary(sample_salaries)
    print(result)