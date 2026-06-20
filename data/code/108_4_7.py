import calendar

def get_day_of_week(year, month, day):
    return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    print(get_day_of_week(2023, 4, 15))