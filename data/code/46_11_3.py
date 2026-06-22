import pandas as pd

def compute_max_salary(records):
    df = pd.DataFrame(records, columns=['name', 'department', 'salary'])
    return df['salary'].max()

if __name__ == '__main__':
    sample_records = [
        ('Alice', 'Engineering', 95000),
        ('Bob', 'Marketing', 65000),
        ('Charlie', 'Engineering', 105000),
        ('Diana', 'HR', 70000),
        ('Eve', 'Marketing', 72000)
    ]
    max_sal = compute_max_salary(sample_records)
    print(max_sal)