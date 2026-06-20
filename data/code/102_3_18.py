import datetime

WEEKDAY_THRESHOLD = 5

def is_weekday():
    current_date = datetime.date.today()
    return current_date.weekday() < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    print(is_weekday())