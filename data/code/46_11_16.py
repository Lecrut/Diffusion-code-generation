import pandas as pd

def compute_max_salary(salary_records):
    df = pd.DataFrame(salary_records, columns=['name', 'salary'])
    return df['salary'].max()

if __name__ == '__main__':
    records = [
        ('Alice', 75000),
        ('Bob', 82000),
        ('Charlie', 69000),
        ('Diana', 91000),
    ]
    result = compute_max_salary(records)
    print(result)