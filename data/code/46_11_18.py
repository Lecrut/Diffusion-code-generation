import pandas as pd

def compute_max_salary(salary_records):
    df = pd.DataFrame(salary_records, columns=['name', 'salary'])
    return df['salary'].max()

if __name__ == '__main__':
    records = [
        ('Alice', 95000),
        ('Bob', 120000),
        ('Charlie', 85000),
        ('Diana', 135000),
        ('Eve', 110000)
    ]
    print(compute_max_salary(records))