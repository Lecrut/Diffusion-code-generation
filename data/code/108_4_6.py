import calendar

def get_day_of_week(year=2023, month=10, day=5):
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    print(get_day_of_week())