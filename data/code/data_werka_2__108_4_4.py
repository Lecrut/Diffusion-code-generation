import calendar

def get_day_of_month(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    if not calendar.isleap(year) and month == 2 and day > 28:
        raise ValueError("Invalid day for February in a non-leap year")
    if month in (4, 6, 9, 11) and day > 30:
        raise ValueError("Invalid day for this month")
    if day > calendar.monthrange(year, month)[1]:
        raise ValueError("Day exceeds the number of days in the month")
    return day

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 15
    result = get_day_of_month(year, month, day)
    print(result)