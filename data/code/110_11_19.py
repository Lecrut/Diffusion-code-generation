from datetime import datetime
from typing import List

def sort_datetimes(datetimes: List[datetime]) -> List[datetime]:
    if not datetimes:
        return []
    
    for item in datetimes:
        if not isinstance(item, datetime):
            raise ValueError("All items must be datetime objects")
            
    return sorted(datetimes)

if __name__ == '__main__':
    dt_2023_may_1 = datetime(2023, 5, 1, 8, 0)
    dt_2022_jan_1 = datetime(2022, 1, 1, 12, 30)
    dt_2024_dec_25 = datetime(2024, 12, 25, 0, 0)
    dt_2023_may_1_copy = datetime(2023, 5, 1, 8, 0)
    
    unsorted_list = [dt_2023_may_1, dt_2022_jan_1, dt_2024_dec_25, dt_2023_may_1_copy]
    
    sorted_result = sort_datetimes(unsorted_list)
    
    print(sorted_result)