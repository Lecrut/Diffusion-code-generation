import pandas as pd

def compute_max_salary(records):
    df = pd.DataFrame(records, columns=['id', 'name', 'salary'])
    return df['salary'].max()

if __name__ == '__main__':
    sample_data = [
        (1, 'Alice', 50000),
        (2, 'Bob', 75000),
        (3, 'Charlie', 65000)
    ]
    result = compute_max_salary(sample_data)
    print(result)