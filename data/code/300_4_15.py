import pandas as pd

def remaining_days_in_month(date):
    date = pd.to_datetime(date)
    end_of_month = (date + pd.offsets.MonthEnd(1)).dt.date[0]
    return (end_of_month - date).days

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(remaining_days_in_month(sample_date))