from datetime import datetime, timedelta
from typing import Union

DATE_FORMAT_CODE = '%Y-%m-%d'
DAY_COUNT_MAP = {
    'days': lambda delta: delta.days,
    'total': lambda delta: int(delta.total_seconds() / 86400),
}

def compute_days_elapsed(start_date_str: str, end_date_str: str, method: str = 'days') -> int:
    if method not in DAY_COUNT_MAP:
        raise ValueError(f"Unsupported method: {method}")
    
    try:
        start_dt = datetime.strptime(start_date_str, DATE_FORMAT_CODE)
        end_dt = datetime.strptime(end_date_str, DATE_FORMAT_CODE)
    except ValueError as e:
        raise ValueError(f"Invalid date format provided: {e}") from e

    difference = end_dt - start_dt
    return DAY_COUNT_MAP[method](difference)

if __name__ == '__main__':
    initial = '2020-02-29'
    final = '2021-03-01'
    result = compute_days_elapsed(initial, final)
    print(result)