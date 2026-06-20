import datetime

def get_current_day_of_week():
    now = datetime.datetime.now()
    day_name = now.strftime("%A")
    return day_name

if __name__ == '__main__':
    print(get_current_day_of_week())