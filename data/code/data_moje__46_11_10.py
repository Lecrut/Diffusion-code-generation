import pandas as pd

def compute_max_salary(salary_column):
    return salary_column.max()

if __name__ == '__main__':
    data = [
        {"employee": "Alice", "salary": 70000},
        {"employee": "Bob", "salary": 85000},
        {"employee": "Charlie", "salary": 60000},
        {"employee": "Diana", "salary": 95000}
    ]
    df = pd.DataFrame(data)
    max_salary = compute_max_salary(df["salary"])
    print(max_salary)