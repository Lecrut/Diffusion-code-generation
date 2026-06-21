import datetime
from typing import List

def sort_iso8601_dates(date_strings: List[str]) -> List[str]:
    if not date_strings:
        return []

    def to_epoch(ds):
        dt = datetime.datetime.fromisoformat(ds)
        return dt.timestamp()

    sorted_pairs = sorted(date_strings, key=to_epoch)
    return sorted_pairs

if __name__ == '__main__':
    sample_dates = [
        "2023-01-01T00:00:00",
        "2020-02-29T12:30:00",
        "2023-10-01T12:00:00",
        "2021-05-15T08:30:00",
        "2022-12-31T23:59:59"
    ]
    sorted_result = sort_iso8601_dates(sample_dates)
    print(sorted_result)