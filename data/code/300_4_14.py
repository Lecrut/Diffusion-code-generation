import pandas as pd

def calculate_remaining_days(date):
    date_obj = pd.to_datetime(date)
    last_day_of_month = date_obj.to_period('M').end_time
    return (last_day_of_month - date_obj).days + 1

if __name__ == '__main__':
    sample_date = '2023-09-25'
    print(calculate_remaining_days(sample_date))