from datetime import date
from typing import List

def sort_date_objects(date_list: List[date]) -> List[date]:
    if not isinstance(date_list, list):
        raise ValueError("Input must be a list")
    if len(date_list) == 0:
        return []
    for item in date_list:
        if not isinstance(item, date):
            raise ValueError("All elements must be date objects")
    return sorted([d for d in date_list])

if __name__ == '__main__':
    my_dates = [date(2024, 1, 1), date(2020, 12, 31), date(2022, 6, 15)]
    ordered = sort_date_objects(my_dates)
    print(ordered)