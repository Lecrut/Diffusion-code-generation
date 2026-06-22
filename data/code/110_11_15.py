from datetime import datetime
from typing import List

SORT_STRATEGY = {
    "ascending": lambda dt: dt,
}

def sort_datetimes(datetimes: List[datetime]) -> List[datetime]:
    if not datetimes:
        return []
    return sorted(datetimes, key=SORT_STRATEGY["ascending"])

if __name__ == '__main__':
    dt_a = datetime(2024, 1, 15, 9, 0)
    dt_b = datetime(2023, 12, 31, 23, 59)
    dt_c = datetime(2024, 2, 1, 0, 0)
    dt_d = datetime(2023, 6, 10, 12, 30)
    
    unsorted_input = [dt_a, dt_b, dt_c, dt_d]
    result = sort_datetimes(unsorted_input)
    
    for item in result:
        print(item)