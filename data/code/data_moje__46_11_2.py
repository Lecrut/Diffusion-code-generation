import pandas as pd

def compute_max_salary(salary_column):
    return salary_column.max()

if __name__ == '__main__':
    data = [
        {"id": 1, "name": "Alice", "salary": 70000},
        {"id": 2, "name": "Bob", "salary": 85000},
        {"id": 3, "name": "Charlie", "salary": 60000},
        {"id": 4, "name": "Diana", "salary": 95000},
        {"id": 5, "name": "Eve", "salary": 72000},
    ]
    df = pd.DataFrame(data)
    max_val = compute_max_salary(df["salary"])
    print(max_val)