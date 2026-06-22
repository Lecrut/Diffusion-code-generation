from datetime import datetime
from typing import List

PARSE_FORMAT: str = "%Y-%m-%dT%H:%M:%S"

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    def parse_date(d: str) -> datetime:
        return datetime.strptime(d, PARSE_FORMAT)
    
    if not date_strings:
        return []
        
    return sorted(date_strings, key=parse_date)

if __name__ == '__main__':
    sample_data = [
        "2023-04-12T10:00:00",
        "2019-11-05T15:30:00",
        "2023-04-12T10:00:01",
        "2020-01-01T00:00:00"
    ]
    sorted_list = sort_iso_dates(sample_data)
    print(sorted_list)