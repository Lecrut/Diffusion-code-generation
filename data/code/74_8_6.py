import datetime

def get_current_day_of_week():
    now = datetime.datetime.now()
    if not isinstance(now, datetime.datetime):
        raise ValueError("Failed to retrieve current date and time")
    
    day_of_week = now.strftime("%A")
    if not isinstance(day_of_week, str) or not day_of_week:
        raise ValueError("Invalid format for day of the week")

    return day_of_week

if __name__ == '__main__':
    print(get_current_day_of_week())