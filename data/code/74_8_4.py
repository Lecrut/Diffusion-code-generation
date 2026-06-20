import datetime

def get_current_day_of_week():
    return datetime.datetime.now().strftime("%A")

if __name__ == '__main__':
    current_time = datetime.datetime.now()
    day_of_week = get_current_day_of_week(current_time)
    print(day_of_week)