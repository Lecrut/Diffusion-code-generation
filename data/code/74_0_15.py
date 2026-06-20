import datetime

def get_current_day_of_week():
    today = datetime.datetime.now()
    day_of_week = today.strftime("%A")
    return day_of_week

if __name__ == '__main__':
    current_day = get_current_day_of_week()
    print(current_day)