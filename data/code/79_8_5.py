from datetime import datetime, timedelta

def first_day_of_next_month(date):
    next_month = date.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(first_day_of_next_month(sample_date))