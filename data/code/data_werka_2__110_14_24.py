from datetime import date
from typing import List

def sort_dates_descending(dates: List[date]) -> List[date]:
    if not dates:
        return []
    return sorted(dates, key=lambda d: d, reverse=True)

if __name__ == '__main__':
    sample_dates = [
        date(2023, 1, 15),
        date(2021, 5, 20),
        date(2024, 12, 31),
        date(2022, 8, 10),
        date(2020, 2, 29),
    ]
    result = sort_dates_descending(sample_dates)
    print(result)