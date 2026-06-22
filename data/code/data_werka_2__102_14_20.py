import calendar

def is_weekday(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False
    try:
        weekday_num = calendar.weekday(year, month, day)
        return weekday_num < 5
    except ValueError:
        return False

if __name__ == '__main__':
    print(is_weekday(2023, 10, 23))
    print(is_weekday(2023, 10, 28))
    print(is_weekday(2023, 2, 29))
    print(is_weekday(2024, 12, 31))
    print(is_weekday(2023, 13, 1))