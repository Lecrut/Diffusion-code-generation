from datetime import datetime
from typing import List

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    parsed_dates = []
    for date_str in date_strings:
        parsed_date = datetime.fromisoformat(date_str)
        parsed_dates.append((parsed_date, date_str))
    parsed_dates.sort(key=lambda item: item[0])
    sorted_dates = [item[1] for item in parsed_dates]
    return sorted_dates

if __name__ == '__main__':
    sample_dates = [
        "2024-01-15T09:30:00",
        "2020-06-20T14:15:00",
        "2023-12-31T23:59:59",
        "2022-02-28T10:00:00",
        "2021-09-10T08:45:00"
    ]
    sorted_result = sort_iso_dates(sample_dates)
    print(sorted_result)