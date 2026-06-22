from datetime import date

_MONTH_TO_INDEX = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7,
    9: 8,
    10: 9,
    11: 10,
    12: 11,
}

def get_day_numeric(year: int, month: int, day: int) -> int:
    target_date = date(year, month, day)
    return target_date.day

if __name__ == '__main__':
    YEAR = 2024
    MONTH = 10
    DAY = 10
    computed_day = get_day_numeric(YEAR, MONTH, DAY)
    print(computed_day)