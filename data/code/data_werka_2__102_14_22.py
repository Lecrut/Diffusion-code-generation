import calendar

WEEKDAY_THRESHOLD = 5

def validate_date_is_weekday(year, month, day):
    day_of_week = calendar.weekday(year, month, day)
    return day_of_week < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    print(validate_date_is_weekday(2023, 10, 23))
    print(validate_date_is_weekday(2023, 10, 28))
    print(validate_date_is_weekday(2023, 2, 29))