from datetime import date

_MONTHS_TO_DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def _is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def _days_in_year(year: int) -> int:
    return 366 if _is_leap_year(year) else 365

def _days_in_month(year: int, month: int) -> int:
    if month == 2 and _is_leap_year(year):
        return 29
    return _MONTHS_TO_DAYS[month]

def calculate_year_difference(date1: date, date2: date) -> int:
    if date1 > date2:
        date1, date2 = date2, date1

    total_days = 0
    current_date = date1

    while current_date.year < date2.year:
        days_in_current_year = _days_in_year(current_date.year)
        days_remaining_in_year = days_in_current_year - current_date.toordinal() + date(1, 1, current_date.year).toordinal()
        total_days += days_remaining_in_year
        current_date = date(current_date.year + 1, 1, 1)

    total_days += date2.toordinal() - current_date.toordinal()

    years = 0
    while total_days >= _days_in_year(date1.year + years):
        years += 1
        total_days -= _days_in_year(date1.year + years - 1)

    return years

if __name__ == '__main__':
    start_date = date(2015, 3, 15)
    end_date = date(2023, 11, 20)
    diff = calculate_year_difference(start_date, end_date)
    print(diff)