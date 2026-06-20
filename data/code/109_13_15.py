import datetime

def days_in_month(year: int, month: int) -> int:
    if month == 12:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        return 29 if is_leap_year else 28

def time_left_in_month(start_date: datetime.date, end_date: datetime.date) -> int:
    assert start_date <= end_date, 'Start date must be before or equal to end date'
    days_left = (end_date - start_date).days
    return max(0, days_left)
if __name__ == '__main__':
    start_date = datetime.date(2023, 10, 15)
    end_date = datetime.date(2024, 1, 15)
    print(time_left_in_month(start_date, end_date))