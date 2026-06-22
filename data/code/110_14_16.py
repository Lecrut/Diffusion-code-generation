from datetime import date, datetime
from typing import List, Union

def _validate_date_input(dates: list) -> None:
    if not isinstance(dates, list):
        raise ValueError("Input must be a list")
    for item in dates:
        if not isinstance(item, (date, datetime)):
            raise ValueError(f"Unsupported type: {type(item)}")

def sort_dates_descending(dates: List[Union[date, datetime]]) -> List[Union[date, datetime]]:
    _validate_date_input(dates)
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