import datetime

def get_current_day_of_week():
    now = datetime.datetime.now()
    return now.strftime('%A')
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5)
    if not isinstance(sample_date, datetime.datetime):
        raise ValueError('Sample date must be a datetime object')
    day_of_week = get_current_day_of_week()
    print(day_of_week)