from datetime import datetime, timedelta

def first_day_next_month(hardcoded_date):
    next_month = hardcoded_date.replace(day=28) + timedelta(days=4)
    return next_month.replace(day=1).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = datetime(2024, 3, 31)
    print(first_day_next_month(sample_date))