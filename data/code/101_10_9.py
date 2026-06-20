import calendar

def get_day_of_week(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    print(get_day_of_week(year, month, day))