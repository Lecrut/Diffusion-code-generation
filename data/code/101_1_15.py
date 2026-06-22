import calendar

def get_weekday_name(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be at least 1")
    try:
        calendar.weekday(year, month, day)
    except ValueError:
        raise ValueError("Invalid date combination")
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 5))