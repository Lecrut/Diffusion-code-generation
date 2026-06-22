import pandas as pd

def compute_max_salary(salary_column):
    return salary_column.max()

if __name__ == '__main__':
    records = [
        {"name": "Alice", "salary": 70000},
        {"name": "Bob", "salary": 120000},
        {"name": "Charlie", "salary": 95000},
        {"name": "Diana", "salary": 110000}
    ]

    df = pd.DataFrame(records)

    result = compute_max_salary(df["salary"])

    print(result)