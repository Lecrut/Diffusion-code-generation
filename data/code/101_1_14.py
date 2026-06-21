import calendar

def get_weekday_name(year, month, day):
    day_number = calendar.weekday(year, month, day)
    name = calendar.day_name[day_number]
    return name

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    computed_name = get_weekday_name(target_year, target_month, target_day)
    print(computed_name)