import datetime

def get_weekday(year, month, day):
    date = datetime.date(year, month, day)
    return date.weekday()

if __name__ == '__main__':
    weekday = get_weekday(2024, 7, 4)
    print(weekday)