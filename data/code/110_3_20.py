from datetime import date
from typing import List

DATE_FORMAT_STRING: str = "%Y-%m-%d"

def sort_date_objects(date_list: List[date]) -> List[date]:
    return [d for d in sorted(date_list)]

if __name__ == '__main__':
    sample_dates: List[date] = [
        date(2024, 5, 10),
        date(2021, 12, 25),
        date(2023, 1, 1),
        date(2022, 8, 15)
    ]
    sorted_result: List[date] = sort_date_objects(sample_dates)
    print(sorted_result)