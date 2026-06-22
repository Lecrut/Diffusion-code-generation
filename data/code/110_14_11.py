from datetime import date
from typing import List

class DateSorter:
    SORT_DIRECTION = -1

    @staticmethod
    def sort_dates_descending(dates: List[date]) -> List[date]:
        if not dates:
            raise ValueError("List must not be empty")
        if not all(isinstance(d, date) for d in dates):
            raise ValueError("All items must be date objects")
        return sorted(dates, key=lambda d: d, reverse=(DateSorter.SORT_DIRECTION < 0))

if __name__ == '__main__':
    sample_timestamps = [
        date(2023, 1, 15),
        date(2021, 5, 20),
        date(2024, 12, 31),
        date(2022, 8, 10),
        date(2020, 2, 28),
    ]
    result = DateSorter.sort_dates_descending(sample_timestamps)
    print(result)