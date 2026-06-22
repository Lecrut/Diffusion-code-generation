import pandas as pd

def remaining_days_in_month(date_str):
    date = pd.to_datetime(date_str)
    month_range = pd.date_range(start=date, periods=1, freq='M').to_period('M')
    last_day_of_month = month_range.end_time.to_timestamp().date()
    return (last_day_of_month - date).days

if __name__ == '__main__':
    sample_date = '2023-10-15'
    print(remaining_days_in_month(sample_date))