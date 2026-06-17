import calendar
def days_remaining(target_month: int, year: int) -> int:
    if target_month < 1 or target_month > 12:
        raise ValueError("Month must be between 1 and 12")
    year_days = 365
    if calendar.isleap(year):
        year_days = 366
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29
    elif year % 4 == 0:
        days_in_month[2] = 29
    elif year % 100 == 0:
        days_in_month[2] = 28
    total_days = days_in_month[target_month]
    return total_days
if __name__ == '__main__':
    print(days_remaining(1, 2023))
    print(days_remaining(12, 2023))
    print(days_remaining(2, 2024))
    print(days_remaining(2, 2023))
    print(days_remaining(2, 2024))