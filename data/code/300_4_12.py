import pandas as pd

def remaining_days_in_month(date):
    end_of_month = pd.to_datetime(date).to_period('M').end_time
    return (end_of_month - pd.to_datetime(date)).days + 1

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(remaining_days_in_month(sample_date))