import calendar

def get_day_of_week(year, month, day):
    day_index = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_index]
    return day_name

if __name__ == '__main__':
    result = get_day_of_week(2023, 12, 25)
    print(result)