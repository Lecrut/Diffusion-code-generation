from datetime import date

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

def get_day_numeric(year: int, month: int, day: int) -> int:
    if month not in _MONTH_NAMES:
        raise ValueError("Invalid month")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    target_date = date(year, month, day)
    return target_date.day

if __name__ == '__main__':
    result = get_day_numeric(2024, 10, 10)
    print(result)