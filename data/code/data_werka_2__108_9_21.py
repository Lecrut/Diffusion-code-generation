from datetime import datetime
from typing import Union

class DateExtractor:
    def __init__(self, reference_date: datetime) -> None:
        if not isinstance(reference_date, datetime):
            raise ValueError("Input must be a datetime instance")
        self.reference_date = reference_date

    def get_day(self) -> int:
        return self.reference_date.day

def extract_day_of_month(dt: datetime) -> int:
    if not isinstance(dt, datetime):
        raise TypeError("Expected datetime object")
    extractor = DateExtractor(dt)
    return extractor.get_day()

if __name__ == '__main__':
    sample_dt = datetime(2024, 12, 25, 8, 0, 0)
    day_value = extract_day_of_month(sample_dt)
    print(day_value)