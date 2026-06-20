import datetime

def get_current_day_of_week():
    current_time = datetime.datetime.now()
    day_of_week = current_time.strftime("%A")
    return day_of_week

if __name__ == '__main__':
    today = get_current_day_of_week()
    print(today)