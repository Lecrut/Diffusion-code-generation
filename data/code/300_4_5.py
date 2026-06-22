import pandas as pd

def remaining_days_in_month(date_str):
    date = pd.to_datetime(date_str)
    last_day_of_month = pd.Timestamp(year=date.year, month=date.month, day=31)
    if date.month == 2:
        last_day_of_month = last_day_of_month.replace(day=28) + pd.Timedelta(days=4)
        last_day_of_month -= pd.Timedelta(days=last_day_of_month.day % 7)
    elif date.month in [4, 6, 9, 11]:
        last_day_of_month = last_day_of_month.replace(day=30)
    return (last_day_of_month - date).days

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(remaining_days_in_month(sample_date))