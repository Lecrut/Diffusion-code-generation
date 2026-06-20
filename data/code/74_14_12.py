import datetime

def get_current_day_of_week():
    current_datetime = datetime.datetime.now()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = current_datetime.weekday()
    return days_of_week[day_index]

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 27)
    day_object = datetime.datetime.combine(sample_date, datetime.time.min)
    result = get_current_day_of_week(day_object)
    print(result)