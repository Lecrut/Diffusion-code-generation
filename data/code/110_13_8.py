from datetime import datetime
from typing import List

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
EMPTY_LIST = []

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    if not date_strings:
        return EMPTY_LIST
    
    def parse_date(date_str: str) -> datetime:
        return datetime.strptime(date_str, DATE_FORMAT)
    
    sorted_dates = sorted(date_strings, key=parse_date)
    return sorted_dates

if __name__ == '__main__':
    sample_dates = [
        "2023-11-15T10:30:00",
        "2021-02-28T14:00:00",
        "2024-01-01T00:00:00",
        "2022-07-04T18:45:00"
    ]
    sorted_result = sort_iso_dates(sample_dates)
    print(sorted_result)