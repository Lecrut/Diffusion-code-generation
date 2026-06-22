from datetime import datetime, timezone
from typing import List

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    def parse_to_timestamp(date_str: str) -> float:
        dt = datetime.fromisoformat(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()

    indexed_dates = []
    for index, date_str in enumerate(date_strings):
        timestamp = parse_to_timestamp(date_str)
        indexed_dates.append((timestamp, index, date_str))

    indexed_dates.sort(key=lambda x: (x[0], x[1]))

    return [item[2] for item in indexed_dates]

if __name__ == '__main__':
    sample_dates = [
        "2024-03-15T10:00:00+00:00",
        "2023-11-20T14:30:00+05:00",
        "2024-03-15T10:00:00-05:00",
        "2022-01-01T00:00:00+00:00",
        "2023-11-20T09:30:00+00:00"
    ]
    sorted_result = sort_iso_dates(sample_dates)
    print(sorted_result)