import calendar

def get_day_of_week(year, month, day):
    return calendar.weekday(year, month, day)

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    day_index = get_day_of_week(year, month, day)
    day_name = calendar.day_name[day_index]
    print(day_name)