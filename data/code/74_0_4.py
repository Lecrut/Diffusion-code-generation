import datetime

def get_current_day_of_week():
    return datetime.datetime.now().strftime("%A")

if __name__ == '__main__':
    day = get_current_day_of_week()
    print(day)