def highest_salary(salaries):
    if not salaries:
        return None
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [3000, 5000, 8000, 4500, 9500, 6000]
    result = highest_salary(sample_salaries)
    print(result)