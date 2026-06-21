import calendar

def get_day_of_month(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    max_days = calendar.monthrange(year, month)[1]
    if day < 1 or day > max_days:
        raise ValueError("Invalid day")
    return day

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = get_day_of_month(year, month, day)
    print(result)