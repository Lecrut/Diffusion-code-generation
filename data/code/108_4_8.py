import calendar

def get_day_of_month(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    if not calendar.monthrange(year, month)[1] >= day:
        raise ValueError("Day is out of range for the given month and year")
    return day

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 15
    result = get_day_of_month(year, month, day)
    print(result)