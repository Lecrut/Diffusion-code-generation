import pandas as pd

def remaining_days_in_month(date):
    df = pd.DataFrame({'date': [date]})
    df['date'] = pd.to_datetime(df['date'])
    last_day_of_month = (df['date'] + pd.offsets.MonthEnd(1)).dt.date[0]
    return (last_day_of_month - date).days

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(remaining_days_in_month(sample_date))