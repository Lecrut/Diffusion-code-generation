import calendar

def get_weekday_for_date(year, month, day):
    if not 1 <= month <= 12:
        raise ValueError("Invalid month")
    max_days = calendar.monthrange(year, month)[1]
    if not 1 <= day <= max_days:
        raise ValueError("Invalid day")
    return calendar.weekday(year, month, day)

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 15
    weekday_index = get_weekday_for_date(year, month, day)
    print(weekday_index)