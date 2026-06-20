import calendar

def get_day_of_week(year, month, day):
    return calendar.monthrange(year, month)[0]

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 5
    print(get_day_of_week(year, month, day))