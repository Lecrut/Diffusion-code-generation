def find_max_salary(salaries):
    if not salaries:
        raise ValueError("List cannot be empty")
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [50000, 75000, 60000, 90000, 85000]
    result = find_max_salary(sample_salaries)
    print(result)