from datetime import date, datetime
from typing import Sequence, TypeVar, Union

DateType = Union[date, datetime]

def validate_dates(items: Sequence[DateType]) -> Sequence[DateType]:
    if not isinstance(items, Sequence):
        raise ValueError("Input must be a sequence")
    for idx, item in enumerate(items):
        if not isinstance(item, (date, datetime)):
            raise ValueError(f"Item at index {idx} is not a date or datetime")
    return items

def sort_timestamps_descending(timestamps: Sequence[DateType]) -> Sequence[DateType]:
    validated = validate_dates(timestamps)
    return sorted(validated, reverse=True)

if __name__ == '__main__':
    raw_timestamps = [
        date(2023, 11, 1),
        datetime(2022, 5, 15, 10, 30),
        date(2024, 1, 1),
        datetime(2020, 12, 25, 0, 0, 0),
    ]
    result = sort_timestamps_descending(raw_timestamps)
    print(result)