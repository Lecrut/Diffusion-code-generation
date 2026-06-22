import calendar

def get_weekday_name(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    if day <= 0:
        raise ValueError("Day must be positive")
    try:
        return calendar.day_name[calendar.weekday(year, month, day)]
    except OverflowError:
        raise ValueError("Date out of valid range")

if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 5))