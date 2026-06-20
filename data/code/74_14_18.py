import datetime

def get_current_day_of_week():
    current_date = datetime.datetime.now()
    return current_date.strftime("%A")

if __name__ == '__main__':
    print(get_current_day_of_week())