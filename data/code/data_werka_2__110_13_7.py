from datetime import datetime
from typing import List

class DateSorter:
    FORMAT_STR = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def parse(date_str: str) -> datetime:
        return datetime.strptime(date_str, DateSorter.FORMAT_STR)

    @staticmethod
    def sort_dates(date_strings: List[str]) -> List[str]:
        if not date_strings:
            return []
        return sorted(date_strings, key=DateSorter.parse)

if __name__ == '__main__':
    sample_dates = [
        "2023-05-15T10:00:00",
        "2021-01-01T00:00:00",
        "2024-12-31T23:59:59",
        "2022-07-20T14:30:00"
    ]
    result = DateSorter.sort_dates(sample_dates)
    print(result)