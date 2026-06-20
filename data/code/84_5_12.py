def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_month(year: int, month: int) -> int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def get_day_number(year: int, month: int, day: int) -> int:
    if not (1 <= month <= 12 and 1 <= day <= days_in_month(year, month)):
        raise ValueError('Invalid date provided')
    total_days = sum((days_in_month(year, m) for m in range(1, month)))
    return total_days + day
if __name__ == '__main__':
    print(get_day_number(2023, 4, 15))