import pandas as pd

def compute_max_salary(salary_records):
    df = pd.DataFrame(salary_records)
    max_salary = df['salary'].max()
    return max_salary

if __name__ == '__main__':
    sample_records = [
        {'id': 1, 'name': 'Alice', 'salary': 75000},
        {'id': 2, 'name': 'Bob', 'salary': 82000},
        {'id': 3, 'name': 'Charlie', 'salary': 68000},
        {'id': 4, 'name': 'Diana', 'salary': 91000},
        {'id': 5, 'name': 'Ethan', 'salary': 77500}
    ]
    result = compute_max_salary(sample_records)
    print(result)