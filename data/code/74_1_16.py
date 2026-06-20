import datetime

DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def get_current_day():
    return DAYS_OF_WEEK[datetime.date.today().weekday()]

if __name__ == '__main__':
    print(get_current_day())