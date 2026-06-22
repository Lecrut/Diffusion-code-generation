def generate_max_salary():
    salaries = [50000, 70000, 65000, 80000, 95000, 75000, 60000]
    return max(salaries)

if __name__ == '__main__':
    result = generate_max_salary()
    print(result)