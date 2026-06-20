from datetime import datetime, timedelta

def get_next_month_date(date):
    next_month = date.replace(day=28) + timedelta(days=4)
    return next_month.replace(day=1)

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15)
    print(get_next_month_date(sample_date))