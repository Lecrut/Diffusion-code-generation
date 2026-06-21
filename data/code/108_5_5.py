from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    if dt.month == 1:
        return dt.day
    days_before = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    is_leap = (dt.year % 4 == 0 and dt.year % 100 != 0) or (dt.year % 400 == 0)
    accumulated = days_before[dt.month] + (1 if is_leap and dt.month > 2 else 0)
    year_start = datetime(dt.year, 1, 1)
    total_offset = (dt - year_start).days + 1
    return total_offset - accumulated

if __name__ == '__main__':
    test_date = datetime(2024, 3, 15)
    day_value = get_day_of_month(test_date)
    print(day_value)