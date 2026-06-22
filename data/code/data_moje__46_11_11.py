import pandas as pd

def compute_max_salary():
    salary_records = [
        {"name": "Alice", "salary": 85000},
        {"name": "Bob", "salary": 92000},
        {"name": "Charlie", "salary": 78000},
        {"name": "Diana", "salary": 105000},
        {"name": "Eve", "salary": 97000}
    ]
    df = pd.DataFrame(salary_records)
    max_salary = df["salary"].max()
    return max_salary

if __name__ == '__main__':
    print(compute_max_salary())