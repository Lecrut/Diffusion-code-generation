def find_highest_salary(salaries):
    if not salaries:
        raise ValueError("List of salaries is empty")
    highest = salaries[0]
    for salary in salaries[1:]:
        if salary > highest:
            highest = salary
    return highest

if __name__ == '__main__':
    sample_salaries = [5000, 8200, 6100, 9500, 7300, 4800]
    print(find_highest_salary(sample_salaries))