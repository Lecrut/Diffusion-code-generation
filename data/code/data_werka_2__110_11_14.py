from datetime import datetime
from typing import List

def validate_datetimes(items):
    for item in items:
        if not isinstance(item, datetime):
            raise ValueError("All elements must be datetime objects")
    return items

def sort_datetimes(datetimes_list: List[datetime]) -> List[datetime]:
    validate_datetimes(datetimes_list)
    return sorted(datetimes_list)

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1)
    dt2 = datetime(2021, 5, 15)
    dt3 = datetime(2022, 1, 1)
    dt4 = datetime(2023, 1, 1)
    sample_list = [dt1, dt2, dt3, dt4]
    result = sort_datetimes(sample_list)
    print(result)