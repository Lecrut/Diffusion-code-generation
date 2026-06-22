from datetime import datetime
from typing import Union

def get_day_of_month(dt: Union[datetime, None]) -> int:
    if dt is None:
        raise ValueError("Input datetime cannot be None")
    if not isinstance(dt, datetime):
        raise TypeError("Input must be a datetime instance")
    return dt.day

if __name__ == '__main__':
    sample_dt = datetime(2024, 12, 25, 10, 0, 0)
    day = get_day_of_month(sample_dt)
    print(day)