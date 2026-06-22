import pandas as pd

def compute_max_salary(salary_records):
    df = pd.DataFrame(salary_records)
    max_salary = df['salary'].max()
    return max_salary

if __name__ == '__main__':
    sample_records = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 82000},
        {'name': 'Charlie', 'salary': 91000},
        {'name': 'Diana', 'salary': 68000},
        {'name': 'Eve', 'salary': 95000}
    ]
    result = compute_max_salary(sample_records)
    print(result)