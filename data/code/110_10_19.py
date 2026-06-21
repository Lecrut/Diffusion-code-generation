from datetime import datetime
from typing import List

def sort_date_strings(date_list: List[str]) -> List[str]:
    if not date_list:
        return []
    return sorted(date_list, key=lambda d: datetime.strptime(d, "%Y-%m-%d"))

if __name__ == '__main__':
    dates = ['2024-02-29', '2023-12-25', '2020-01-01', '2023-01-01']
    result = sort_date_strings(dates)
    print(result)