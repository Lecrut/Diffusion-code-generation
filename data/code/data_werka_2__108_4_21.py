import calendar

WEEKDAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def get_day_of_month(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    days_in_month = calendar.monthrange(year, month)[1]
    if day > days_in_month:
        raise ValueError("Day out of range")
    weekday_index = calendar.weekday(year, month, day)
    return WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = get_day_of_month(year, month, day)
    print(result)