import pandas as pd

def compute_max_salary(records):
    df = pd.DataFrame(records)
    max_salary = df['salary'].max()
    return max_salary

if __name__ == '__main__':
    salary_data = [
        {"name": "Alice", "salary": 75000},
        {"name": "Bob", "salary": 82000},
        {"name": "Charlie", "salary": 95000},
        {"name": "Diana", "salary": 68000},
        {"name": "Eve", "salary": 105000}
    ]
    result = compute_max_salary(salary_data)
    print(result)