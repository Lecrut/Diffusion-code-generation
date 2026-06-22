import calendar

def get_day_of_month(year, month, day):
    if not calendar.isleap(year) and month == 2 and day == 29:
        raise ValueError("Invalid date: February 29 does not exist in non-leap years.")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31.")
    if day > calendar.monthrange(year, month)[1]:
        raise ValueError("Day exceeds the number of days in the specified month.")
    return day

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 15
    result = get_day_of_month(year, month, day)
    print(result)