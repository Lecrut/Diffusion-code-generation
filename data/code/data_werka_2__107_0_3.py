from datetime import datetime

_MONTH_NAMES = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
    5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
    9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}

def format_iso8601(dt: datetime) -> str:
    year = dt.year
    month_num = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    month_label = _MONTH_NAMES[month_num]
    return f"{year}-{month_num:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    output = format_iso8601(sample_dt)
    print(output)