from datetime import datetime
from typing import Union

DAY_MAP = {
    "day": lambda dt: dt.day,
    "month": lambda dt: dt.month,
    "year": lambda dt: dt.year,
}

def get_day_of_month(dt: Union[datetime, int, float]) -> int:
    if isinstance(dt, (int, float)):
        converted_dt = datetime.fromtimestamp(dt)
    elif isinstance(dt, datetime):
        converted_dt = dt
    else:
        raise ValueError(f"Unsupported type {type(dt)}")
    
    extractor = DAY_MAP["day"]
    return extractor(converted_dt)

if __name__ == '__main__':
    sample_dt = datetime(2024, 2, 29, 10, 0, 0)
    output = get_day_of_month(sample_dt)
    print(output)