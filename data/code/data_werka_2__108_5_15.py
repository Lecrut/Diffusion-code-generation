from datetime import datetime
from typing import Union

def get_day_of_month(dt: Union[datetime, int, int, int]) -> int:
    if isinstance(dt, int):
        year, month, day = dt, 1, 1
        dt = datetime(year, month, day)
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object or a tuple/list of (year, month, day)")
    if dt.day < 1 or dt.day > 31:
        raise ValueError("Invalid day value")
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2024, 2, 29)
    day_value = get_day_of_month(sample_date)
    print(day_value)