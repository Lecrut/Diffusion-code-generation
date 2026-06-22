from datetime import datetime
from typing import List

TIMESTAMP_FORMAT: str = "%Y-%m-%d %H:%M:%S"
DEFAULT_SAMPLE_DATETIME: datetime = datetime(1970, 1, 1)

def sort_datetimes(datetimes_list: List[datetime]) -> List[datetime]:
    if not datetimes_list:
        return []
    return sorted(datetimes_list)

if __name__ == '__main__':
    sample_dates: List[datetime] = [
        datetime(2023, 10, 1),
        datetime(2021, 5, 15),
        datetime(2022, 1, 1),
        datetime(2023, 1, 1),
    ]
    sorted_dates: List[datetime] = sort_datetimes(sample_dates)
    for date in sorted_dates:
        print(date.strftime(TIMESTAMP_FORMAT))