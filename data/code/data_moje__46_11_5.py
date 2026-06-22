import pandas as pd

def compute_max_salary(records):
    df = pd.DataFrame(records, columns=["name", "salary"])
    return df["salary"].max()

if __name__ == "__main__":
    sample_records = [
        ("Alice", 75000),
        ("Bob", 82000),
        ("Charlie", 68000),
        ("Diana", 91000),
        ("Eve", 79000)
    ]
    result = compute_max_salary(sample_records)
    print(result)