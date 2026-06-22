def find_highest_salary(salaries):
    if not salaries:
        return None
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [50000, 60000, 75000, 55000, 80000, 70000]
    result = find_highest_salary(sample_salaries)
    print(result)