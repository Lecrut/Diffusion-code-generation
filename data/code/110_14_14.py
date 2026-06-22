from datetime import date, datetime
from typing import List, Union
import operator

class DateSorter:
    def __init__(self, dates: List[Union[date, datetime]]):
        if not isinstance(dates, list):
            raise ValueError("Input must be a list")
        for i, d in enumerate(dates):
            if not isinstance(d, (date, datetime)):
                raise ValueError(f"Element at index {i} is not a date or datetime object")
        self._dates = list(dates)

    def get_sorted_descending(self) -> List[Union[date, datetime]]:
        return sorted(self._dates, key=operator.attrgetter('timetuple'), reverse=True)

if __name__ == '__main__':
    raw_dates = [
        date(2020, 1, 1),
        datetime(2023, 6, 15, 10, 30),
        date(2021, 11, 11),
        datetime(1999, 12, 31, 23, 59, 59),
    ]
    sorter = DateSorter(raw_dates)
    result = sorter.get_sorted_descending()
    print(result)