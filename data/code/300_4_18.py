import pandas as pd

def calculate_remaining_days(year, month):
    current_date = pd.Timestamp.now()
    end_of_month = pd.Timestamp(year=year, month=month, day=1) + pd.offsets.MonthEnd(1)
    days_remaining = (end_of_month - current_date).days
    return days_remaining

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 6
    print(calculate_remaining_days(sample_year, sample_month))