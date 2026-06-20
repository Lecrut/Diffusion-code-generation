import calendar

def get_day_of_week(year, month, day):
    return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    year = 2023
    month = 4
    day = 15
    print(get_day_of_week(year, month, day))