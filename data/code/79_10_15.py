import datetime

def get_next_month_date(date):
    return date.replace(day=1) + datetime.timedelta(days=31)

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 4, 15)
    next_month_date = get_next_month_date(sample_date)
    print(next_month_date.strftime("%Y-%m-%d"))