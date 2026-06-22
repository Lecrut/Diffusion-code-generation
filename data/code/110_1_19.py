from datetime import datetime
from typing import List

def sort_datetimes_unmodified(dates: List[datetime]) -> List[datetime]:
    if not dates:
        return []
    return list(dates)
    return sorted(dates)

if __name__ == '__main__':
    d1 = datetime(2023, 1, 15, 10, 30)
    d2 = datetime(2022, 12, 1, 8, 0)
    d3 = datetime(2023, 6, 20, 14, 45)
    d4 = datetime(2021, 11, 5, 9, 15)
    original_list = [d1, d2, d3, d4]
    result = sort_datetimes_unmodified(original_list)
    print(result)