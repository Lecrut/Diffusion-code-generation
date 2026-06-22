def find_highest_salary(salaries):
    if not salaries:
        raise ValueError("The list of salaries cannot be empty.")
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 23000, 105000, 67000, 99000]
    result = find_highest_salary(sample_salaries)
    print(result)