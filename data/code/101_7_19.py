import datetime

def get_weekday(year, month, day):
    date_obj = datetime.date(year, month, day)
    return date_obj.weekday()

if __name__ == '__main__':
    weekday = get_weekday(2024, 7, 4)
    print(weekday)