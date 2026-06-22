from datetime import datetime
from typing import List

def sort_datetimes(datetimes_list: List[datetime]) -> List[datetime]:
    if not isinstance(datetimes_list, list):
        raise ValueError("Input must be a list")
    for item in datetimes_list:
        if not isinstance(item, datetime):
            raise ValueError("All items must be datetime objects")
    return sorted(datetimes_list)

if __name__ == '__main__':
    dt_1 = datetime(2023, 10, 1)
    dt_2 = datetime(2021, 5, 15)
    dt_3 = datetime(2022, 1, 1)
    dt_4 = datetime(2023, 1, 1)
    sample_datetimes = [dt_1, dt_2, dt_3, dt_4]
    sorted_result = sort_datetimes(sample_datetimes)
    print(sorted_result)