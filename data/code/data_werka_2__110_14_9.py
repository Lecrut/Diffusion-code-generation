from datetime import date, datetime
from typing import List, Union

def sort_dates_descending(dates: List[Union[date, datetime]]) -> List[Union[date, datetime]]:
    return sorted(dates, reverse=True)

if __name__ == '__main__':
    sample_dates = [
        date(2023, 1, 15),
        date(2021, 12, 31),
        date(2024, 6, 1),
        date(2022, 3, 10),
    ]
    sorted_dates = sort_dates_descending(sample_dates)
    print(sorted_dates)