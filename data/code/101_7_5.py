import datetime

def get_weekday(year, month, day):
    date_object = datetime.date(year, month, day)
    return date_object.weekday()

if __name__ == '__main__':
    year = 2024
    month = 7
    day = 4
    print(get_weekday(year, month, day))