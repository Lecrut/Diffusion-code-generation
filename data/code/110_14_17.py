from datetime import date, datetime
from typing import List

def sort_dates_descending(dates: List[date]) -> List[date]:
    return sorted(dates, reverse=True)

if __name__ == '__main__':
    sample_dates = [
        date(2023, 1, 15),
        date(2021, 5, 20),
        date(2024, 12, 31),
        date(2022, 8, 10),
    ]
    sorted_dates = sort_dates_descending(sample_dates)
    print(sorted_dates)