from datetime import datetime, timezone
from typing import List

PARSE_FORMAT = "%Y-%m-%dT%H:%M:%S"
UTC_OFFSET = timezone.utc

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    def parse_date(date_str: str) -> datetime:
        if date_str.endswith('Z'):
            local_dt = datetime.strptime(date_str[:-1], PARSE_FORMAT)
            return local_dt.replace(tzinfo=UTC_OFFSET)
        return datetime.strptime(date_str, PARSE_FORMAT)
    
    sorted_dates = sorted(date_strings, key=parse_date)
    return sorted_dates

if __name__ == '__main__':
    sample_dates = [
        "2023-10-01T12:00:00Z",
        "2021-05-15T08:30:00",
        "2023-01-01T00:00:00",
        "2022-12-31T23:59:59"
    ]
    result = sort_iso_dates(sample_dates)
    print(result)