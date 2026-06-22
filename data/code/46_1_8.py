def highest_salary(salaries):
    if not salaries:
        return None
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [5000, 7500, 3000, 9000, 4500]
    result = highest_salary(sample_salaries)
    print(result)