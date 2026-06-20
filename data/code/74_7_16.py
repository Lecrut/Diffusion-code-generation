import datetime

def get_current_day_of_week():
    current_date = datetime.datetime.now()
    day_of_week = current_date.strftime("%A")
    return day_of_week

if __name__ == '__main__':
    print(get_current_day_of_week())