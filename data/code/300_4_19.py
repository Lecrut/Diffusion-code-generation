import pandas as pd

def remaining_days_in_month(date_str):
    date = pd.to_datetime(date_str)
    first_day_of_next_month = pd.Timestamp(year=date.year, month=date.month + 1, day=1)
    return (first_day_of_next_month - date).days - 1

if __name__ == '__main__':
    sample_date = '2023-10-15'
    print(remaining_days_in_month(sample_date))