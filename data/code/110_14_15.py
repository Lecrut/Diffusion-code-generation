from datetime import date
from typing import List

class DateSorter:
    def __init__(self, dates: List[date]):
        self.dates = list(dates)

    def sort_descending(self) -> List[date]:
        return sorted(self.dates, reverse=True)

    def get_latest(self) -> date:
        if not self.dates:
            raise ValueError("Cannot get latest date from empty list")
        return max(self.dates)

    def get_earliest(self) -> date:
        if not self.dates:
            raise ValueError("Cannot get earliest date from empty list")
        return min(self.dates)

if __name__ == '__main__':
    sample_dates = [
        date(2023, 1, 15),
        date(2021, 5, 20),
        date(2024, 12, 31),
        date(2022, 8, 10),
    ]
    sorter = DateSorter(sample_dates)
    print(sorter.sort_descending())
    print(sorter.get_latest())
    print(sorter.get_earliest())