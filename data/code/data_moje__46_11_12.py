import pandas as pd

def get_max_salary(salary_records):
    df = pd.DataFrame(salary_records)
    return df['salary'].max()

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'salary': 50000},
        {'id': 2, 'name': 'Bob', 'salary': 75000},
        {'id': 3, 'name': 'Charlie', 'salary': 60000},
        {'id': 4, 'name': 'David', 'salary': 82000},
        {'id': 5, 'name': 'Eve', 'salary': 45000}
    ]
    print(get_max_salary(sample_data))