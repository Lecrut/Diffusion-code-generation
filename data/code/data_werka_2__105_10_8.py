from datetime import datetime
from calendar import monthrange

def get_next_day(date_str: str) -> datetime:
    year, month, day = map(int, date_str.split('-'))
    _, days_in_month = monthrange(year, month)
    if day < days_in_month:
        return datetime(year, month, day + 1)
    if month < 12:
        return datetime(year, month + 1, 1)
    return datetime(year + 1, 1, 1)

if __name__ == '__main__':
    sample_date = '2024-12-31'
    result = get_next_day(sample_date)
    print(result)