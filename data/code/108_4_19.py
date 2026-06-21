import calendar

def get_day_of_month(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    if not calendar.monthrange(year, month)[1] >= day:
        raise ValueError("Day out of range for the given month and year")
    return day

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 15
    result = get_day_of_month(year, month, day)
    print(result)