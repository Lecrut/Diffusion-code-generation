import pandas as pd

def days_remaining_in_month(date_str):
    date = pd.to_datetime(date_str)
    last_day_of_month = pd.Timestamp(year=date.year, month=date.month + 1, day=1) - pd.Timedelta(days=1)
    return (last_day_of_month - date).days

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(days_remaining_in_month(sample_date))