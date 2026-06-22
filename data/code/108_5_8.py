from datetime import datetime
from calendar import monthrange

def get_day_of_month(dt: datetime) -> int:
    _, last_day = monthrange(dt.year, dt.month)
    if dt.day > last_day:
        raise ValueError("Invalid day for given month and year")
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2024, 2, 29)
    result = get_day_of_month(sample_date)
    print(result)