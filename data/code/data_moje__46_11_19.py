import pandas as pd

def compute_max_salary(data):
    df = pd.DataFrame(data, columns=['name', 'salary'])
    return df['salary'].max()

if __name__ == '__main__':
    salaries = [
        ('Alice', 85000),
        ('Bob', 92000),
        ('Charlie', 78000),
        ('Diana', 95000)
    ]
    result = compute_max_salary(salaries)
    print(result)