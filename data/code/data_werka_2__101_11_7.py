import calendar

def get_day_of_week(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    max_day = calendar.monthrange(year, month)[1]
    if not (1 <= day <= max_day):
        raise ValueError("Invalid day for the given month and year")
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)