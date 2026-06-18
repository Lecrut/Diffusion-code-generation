import pandas as pd
def add_months_to_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if 'date' not in df.columns:
        raise ValueError("DataFrame must contain a 'date' column.")
    df['date'] = pd.to_datetime(df['date'])
    month_adds = {0: [df.index]}.get(0, [])
    df['months_to_add'] = range(len(df))
    df['new_date'] = df['date'].dt.to_period('M') + df['months_to_add'].astype(int) - 1
    return df
if __name__ == '__main__':
    sample_data = {
        'id': [1, 2, 3],
        'date': ['2023-01-15', '2023-06-20', '2024-09-10'],
        'value': [10.5, 20.75, 30]
    }
    df = pd.DataFrame(sample_data)
    result_df = add_months_to_column(df)
    print(result_df.to_string())