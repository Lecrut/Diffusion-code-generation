import calendar

def get_day_of_week(date_string: str) -> int:
    year_part = int(date_string[:4])
    month_part = int(date_string[5:7])
    day_part = int(date_string[8:10])
    return calendar.weekday(year_part, month_part, day_part)

if __name__ == '__main__':
    print(get_day_of_week("1985-04-12"))
    print(get_day_of_week("2020-02-29"))
    print(get_day_of_week("2021-12-31"))