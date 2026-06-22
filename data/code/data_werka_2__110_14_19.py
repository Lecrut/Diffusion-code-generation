from datetime import date, datetime
from typing import List, Union
from collections.abc import Iterable

class DateSorter:
    def __init__(self, dates: Iterable[Union[date, datetime]]):
        self.dates = list(dates)
        self._validate()

    def _validate(self):
        for item in self.dates:
            if not isinstance(item, (date, datetime)):
                raise ValueError(f"Unsupported type: {type(item)}")

    def sort_descending(self) -> List[Union[date, datetime]]:
        return sorted(self.dates, reverse=True)

if __name__ == '__main__':
    sample_dates = [
        date(2023, 1, 15),
        date(2021, 5, 20),
        date(2024, 12, 31),
        date(2022, 8, 10),
    ]
    sorter = DateSorter(sample_dates)
    result = sorter.sort_descending()
    print(result)