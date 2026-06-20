def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_month(year: int, month: int) -> int:
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        months[2] = 29
    return months[month]

def get_day_number(year: int, month: int, day: int) -> int:
    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError('Invalid date provided')
    day_of_year = sum((days_in_month(year, m) for m in range(1, month))) + day
    return day_of_year
if __name__ == '__main__':
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2023, 2, 28))