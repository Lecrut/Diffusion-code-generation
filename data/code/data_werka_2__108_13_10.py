from datetime import date

def get_numeric_day(year: int, month: int, day: int) -> int:
    validation_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        max_days = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    else:
        max_days = validation_days[month - 1]
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= max_days):
        raise ValueError("Invalid day")
    return date(year, month, day).day

if __name__ == '__main__':
    print(get_numeric_day(2024, 10, 10))