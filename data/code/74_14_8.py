import datetime

def get_current_day_of_week():
    today = datetime.datetime.now()
    day_index = today.weekday()
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    return days_of_week[day_index]

if __name__ == '__main__':
    sample_day_of_week = get_current_day_of_week()
    print(sample_day_of_week)