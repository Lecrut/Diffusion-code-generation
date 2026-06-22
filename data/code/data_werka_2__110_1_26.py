from datetime import datetime
from typing import List

def sort_datetimes_unmodified(dates: List[datetime]) -> List[datetime]:
    if not isinstance(dates, list):
        raise ValueError("Input must be a list")
    for item in dates:
        if not isinstance(item, datetime):
            raise ValueError("All elements must be datetime objects")
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 10, 1),
        datetime(2021, 5, 15),
        datetime(2022, 1, 1),
        datetime(2023, 10, 1, 12, 0, 0)
    ]
    original_copy = list(sample_dates)
    sorted_dates = sort_datetimes_unmodified(sample_dates)
    print(sorted_dates)
    print(original_copy)