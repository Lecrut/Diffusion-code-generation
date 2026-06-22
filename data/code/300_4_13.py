import pandas as pd
ONE_MONTH = pd.DateOffset(months=1)

def calculate_remaining_days(date):
    date = pd.to_datetime(date)
    end_of_month = (date + ONE_MONTH).replace(day=1) - pd.DateOffset(days=1)
    return (end_of_month - date).days
if __name__ == '__main__':
    sample_date = '2023-10-15'
    print(calculate_remaining_days(sample_date))