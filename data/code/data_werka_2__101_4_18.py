import calendar

def get_day_of_week(date_string: str) -> int:
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:10])
    return calendar.weekday(year, month, day)

if __name__ == '__main__':
    print(get_day_of_week("2023-10-23"))
    print(get_day_of_week("2024-01-01"))
    print(get_day_of_week("2000-02-29"))