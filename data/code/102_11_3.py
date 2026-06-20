import datetime

def is_weekday(date_str):
    year, month, day = map(int, date_str.split('-'))
    return datetime.date(year, month, day).weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-06'))
    print(is_weekday('2023-10-07'))