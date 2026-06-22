import calendar

def get_weekday_name(year, month, day):
    day_of_week = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_of_week]
    return str(day_name)

if __name__ == '__main__':
    year_val = 2000
    month_val = 1
    day_val = 1
    result = get_weekday_name(year_val, month_val, day_val)
    print(result)