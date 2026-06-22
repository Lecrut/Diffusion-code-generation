import calendar

_DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def get_weekday_name(year: int, month: int, day: int) -> str:
    weekday_index = calendar.weekday(year, month, day)
    return _DAYS_OF_WEEK[weekday_index]

if __name__ == '__main__':
    result = get_weekday_name(2023, 10, 5)
    print(result)