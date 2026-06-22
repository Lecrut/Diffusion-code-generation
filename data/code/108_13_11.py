from datetime import date

def get_numeric_day(year: int, month: int, day: int) -> int:
    _MONTH_NAME_MAP = {
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
    if not 1 <= month <= 12:
        raise ValueError(f"Invalid month: {month}")
    if not 1 <= day <= 31:
        raise ValueError(f"Invalid day: {day}")
    try:
        date_obj = date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    return date_obj.day

if __name__ == '__main__':
    target_year = 2024
    target_month = 10
    target_day = 10
    day_numeric = get_numeric_day(target_year, target_month, target_day)
    print(day_numeric)