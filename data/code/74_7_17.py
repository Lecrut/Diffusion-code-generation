import datetime

def get_current_day_of_week():
    now = datetime.datetime.now()
    return now.strftime("%A")

if __name__ == '__main__':
    day_name = get_current_day_of_week()
    print(day_name)