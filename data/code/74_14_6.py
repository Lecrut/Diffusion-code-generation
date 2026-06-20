import datetime

def get_current_day_of_week():
    current_time = datetime.datetime.now()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = current_time.weekday()
    return days_of_week[day_index]

if __name__ == '__main__':
    sample_date = "2023-10-27"
    date_object = datetime.datetime.strptime(sample_date, "%Y-%m-%d")
    day_of_week = get_current_day_of_week(date_object)
    print(day_of_week)