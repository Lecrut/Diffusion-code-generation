import datetime

def get_current_day_of_week():
    current_time = datetime.datetime.now()
    day_of_week = current_time.strftime('%A')
    return day_of_week
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5)
    day = get_current_day_of_week(sample_date)
    print(day)