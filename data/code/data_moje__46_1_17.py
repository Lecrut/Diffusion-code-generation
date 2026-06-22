def find_max_salary(salaries):
    if not salaries:
        raise ValueError("List is empty")
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [50000, 60000, 75000, 45000, 80000, 55000]
    result = find_max_salary(sample_salaries)
    print(result)