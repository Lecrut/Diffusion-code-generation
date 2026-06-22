import pandas as pd

def get_max_salary(data: list) -> float:
    df = pd.DataFrame(data, columns=["Name", "Salary"])
    return df["Salary"].max()

if __name__ == '__main__':
    records = [
        ["Alice", 70000],
        ["Bob", 85000],
        ["Charlie", 60000],
        ["Diana", 95000],
        ["Eve", 55000]
    ]
    max_salary = get_max_salary(records)
    print(max_salary)