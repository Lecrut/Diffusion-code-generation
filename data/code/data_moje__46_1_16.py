def highest_salary(salaries):
    if not salaries:
        return None
    highest = salaries[0]
    for i in range(1, len(salaries)):
        if salaries[i] > highest:
            highest = salaries[i]
    return highest

if __name__ == '__main__':
    sample_salaries = [50000, 120000, 75000, 90000, 30000]
    result = highest_salary(sample_salaries)
    print(result)