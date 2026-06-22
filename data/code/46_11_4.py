import pandas as pd

def compute_max_salary(records):
    df = pd.DataFrame(records, columns=['id', 'salary'])
    return df['salary'].max()

if __name__ == '__main__':
    salaries = [
        {'id': 1, 'salary': 50000},
        {'id': 2, 'salary': 60000},
        {'id': 3, 'salary': 75000},
        {'id': 4, 'salary': 45000},
        {'id': 5, 'salary': 80000}
    ]
    result = compute_max_salary(salaries)
    print(result)