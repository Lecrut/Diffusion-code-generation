import pandas as pd

def compute_max_salary(salary_records):
    df = pd.DataFrame(salary_records)
    max_salary = df['salary'].max()
    return max_salary

if __name__ == '__main__':
    records = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 120000},
        {'name': 'Charlie', 'salary': 85000},
        {'name': 'Diana', 'salary': 110000},
        {'name': 'Eve', 'salary': 105000}
    ]
    result = compute_max_salary(records)
    print(result)