import sys

def find_max_salary(salary_strings):
    max_salary = float('-inf')
    for salary_str in (float(s.strip()) for s in salary_strings if s.strip()):
        if salary_str > max_salary:
            max_salary = salary_str
    return max_salary

if __name__ == '__main__':
    salaries = [
        "50000.50",
        "62000.00",
        "45000.75",
        "78000.25",
        "39000.90",
        "55000.00",
        "67000.15",
        "82000.50"
    ]
    result = find_max_salary(salaries)
    print(result)