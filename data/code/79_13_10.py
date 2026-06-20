import datetime

def get_next_month_date(start_date):
    next_month = start_date.replace(day=1) + datetime.timedelta(days=32)
    return next_month.replace(day=1)

if __name__ == '__main__':
    start_date = datetime.date(2023, 1, 15)
    next_month_date = get_next_month_date(start_date)
    print(next_month_date.strftime('%Y-%m-%d'))