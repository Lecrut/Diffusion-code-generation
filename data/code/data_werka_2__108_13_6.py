from datetime import date
import calendar

_MONTH_NAMES = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

def _validate_date_components(year: int, month: int, day: int) -> None:
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError("Year must be an integer")
    if not isinstance(month, int) or isinstance(month, bool):
        raise TypeError("Month must be an integer")
    if not isinstance(day, int) or isinstance(day, bool):
        raise TypeError("Day must be an integer")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    max_days = calendar.monthrange(year, month)[1]
    if day < 1 or day > max_days:
        raise ValueError(f"Day must be between 1 and {max_days} for {month}/{year}")

def get_day_of_month(year: int, month: int, day: int) -> int:
    _validate_date_components(year, month, day)
    target = date(year, month, day)
    return target.day

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 10
    sample_day = 10
    day_numeric = get_day_of_month(sample_year, sample_month, sample_day)
    print(day_numeric)