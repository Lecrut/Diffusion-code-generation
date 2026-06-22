import calendar

def get_day_of_week(year, month, day):
    return calendar.weekday(year, month, day)

if __name__ == '__main__':
    result = get_day_of_week(2025, 3, 15)
    print(result)