from datetime import datetime
from typing import List

def sort_datetimes_ascending(dates: List[datetime]) -> List[datetime]:
    if not isinstance(dates, list):
        raise ValueError("Input must be a list")
    for item in dates:
        if not isinstance(item, datetime):
            raise ValueError("All elements must be datetime objects")
    return sorted(dates, key=lambda x: x.timestamp())

if __name__ == '__main__':
    dt_a = datetime(2024, 2, 10, 8, 0, 0)
    dt_b = datetime(2023, 12, 25, 14, 30, 0)
    dt_c = datetime(2024, 2, 10, 8, 0, 0)
    dt_d = datetime(2025, 1, 1, 0, 0, 0)
    unsorted_times = [dt_a, dt_d, dt_b, dt_c]
    sorted_times = sort_datetimes_ascending(unsorted_times)
    print(sorted_times)