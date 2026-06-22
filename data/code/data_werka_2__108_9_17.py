from datetime import datetime
from typing import Union

class DateExtractor:
    def __init__(self, reference_date: datetime) -> None:
        if not isinstance(reference_date, datetime):
            raise ValueError("Input must be a datetime instance")
        self._date = reference_date

    def get_day(self) -> int:
        return self._date.day

def extract_day(dt: datetime) -> int:
    if not isinstance(dt, datetime):
        raise TypeError("Expected datetime type")
    extractor = DateExtractor(dt)
    return extractor.get_day()

if __name__ == '__main__':
    sample_dt = datetime(2024, 2, 29, 0, 0, 0)
    day_value = extract_day(sample_dt)
    print(day_value)