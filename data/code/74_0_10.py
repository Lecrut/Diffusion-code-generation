import datetime

def get_current_day_of_week():
    today = datetime.datetime.now()
    day_number = today.weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days_of_week[day_number]
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    sample_datetime = datetime.datetime.combine(sample_date, datetime.time())
    day_name = get_current_day_of_week()
    print(day_name)