def max_salary_generator(salaries):
    max_sal = max(salaries)
    for salary in salaries:
        if salary == max_sal:
            yield max_sal

if __name__ == '__main__':
    salary_data = [50000, 120000, 75000, 90000, 120000, 45000]
    result = list(max_salary_generator(salary_data))
    print(result)