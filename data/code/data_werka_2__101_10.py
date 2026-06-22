import calendar

def get_day_of_week(year, month, day):
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index]

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    result = get_day_of_week(year, month, day)
    print(result)