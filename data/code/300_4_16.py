import pandas as pd

def remaining_days_in_month(date_str):
    date = pd.to_datetime(date_str)
    next_month_first_day = pd.to_datetime(f"{date.year}-{date.month+1}-01")
    last_day_of_current_month = next_month_first_day - pd.Timedelta(days=1)
    return (last_day_of_current_month - date).days

if __name__ == '__main__':
    sample_date = '2023-10-15'
    print(remaining_days_in_month(sample_date))