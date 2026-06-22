import pandas as pd

def compute_max_salary(salary_records):
    df = pd.DataFrame(salary_records, columns=['name', 'salary'])
    return df['salary'].max()

if __name__ == '__main__':
    records = [
        ('Alice', 50000),
        ('Bob', 60000),
        ('Charlie', 75000),
        ('Diana', 65000),
        ('Eve', 55000)
    ]
    max_sal = compute_max_salary(records)
    print(max_sal)