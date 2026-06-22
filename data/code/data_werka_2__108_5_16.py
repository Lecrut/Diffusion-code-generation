from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    days_in_month_map = {
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
        12: 31
    }
    is_leap = (dt.year % 4 == 0 and dt.year % 100 != 0) or (dt.year % 400 == 0)
    if dt.month == 2 and is_leap:
        days_in_month_map[2] = 29
    if dt.day > days_in_month_map[dt.month]:
        raise ValueError(f"Invalid day {dt.day} for month {dt.month} in year {dt.year}")
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2024, 2, 29)
    result = get_day_of_month(sample_date)
    print(result)