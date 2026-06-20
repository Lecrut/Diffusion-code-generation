import calendar

def get_day_of_week(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 5
    print(get_day_of_week(year, month, day))