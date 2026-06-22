from datetime import datetime, timedelta
from typing import Dict

UNIT_MAPPING: Dict[str, int] = {
    "hours": 3600,
    "minutes": 60,
    "seconds": 1,
}

def get_time_components(
    start_dt: datetime,
    end_dt: datetime
) -> Dict[str, int]:
    delta: timedelta = end_dt - start_dt
    total_secs: int = int(delta.total_seconds())
    abs_secs: int = abs(total_secs)
    sign: int = -1 if total_secs < 0 else 1
    units: Dict[str, int] = {}
    for unit, divisor in UNIT_MAPPING.items():
        count, abs_secs = divmod(abs_secs, divisor)
        units[unit] = sign * count
    return units

if __name__ == '__main__':
    start_time: datetime = datetime(2023, 10, 1, 8, 0, 0)
    end_time: datetime = datetime(2023, 10, 1, 12, 30, 45)
    result: Dict[str, int] = get_time_components(start_time, end_time)
    print(result)