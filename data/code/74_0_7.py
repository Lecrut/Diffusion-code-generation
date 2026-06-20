import datetime

def get_current_day_of_week():
    current_time = datetime.datetime.now()
    day_of_week_index = current_time.weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days_of_week[day_of_week_index]
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5)
    day = get_current_day_of_week()
    print(day)