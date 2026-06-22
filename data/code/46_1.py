def find_highest_salary(salaries):
    if not salaries:
        return None
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    salaries = [50000, 120000, 85000, 95000, 60000]
    result = find_highest_salary(salaries)
    print(result)