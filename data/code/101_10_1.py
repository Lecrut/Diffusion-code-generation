import calendar

def get_day_of_week(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    print(get_day_of_week(2023, 12, 25))