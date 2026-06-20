import datetime

def get_next_wednesday(start_date):
    current_day = start_date.weekday()
    days_until_wednesday = (2 - current_day) % 7
    next_wednesday = start_date + datetime.timedelta(days=days_until_wednesday)
    return next_wednesday

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 10)
    next_wednesday = get_next_wednesday(sample_date)
    print(next_wednesday.strftime("%Y-%m-%d"))