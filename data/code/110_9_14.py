from datetime import datetime
from typing import List

def sort_date_strings(date_strings: List[str]) -> List[str]:
    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%m-%d-%Y",
        "%m/%d/%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%d-%m-%Y %H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
        "%m-%d-%Y %H:%M:%S",
        "%m/%d/%Y %H:%M:%S",
    ]

    def parse_date(date_str: str) -> datetime:
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Unsupported date format: {date_str}")

    parsed_dates = []
    for date_str in date_strings:
        dt = parse_date(date_str)
        parsed_dates.append((dt, date_str))

    parsed_dates.sort(key=lambda x: x[0])

    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "15/01/2023",
        "2023/01/15",
        "01-15-2023",
        "2023-01-15 10:30:00",
        "15/01/2023 10:30:00",
    ]
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)