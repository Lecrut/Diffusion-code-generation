from datetime import datetime
from typing import List

def sort_date_strings(date_strings: List[str]) -> List[str]:
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m-%d-%Y",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%Y.%m.%d",
        "%d.%m.%Y",
        "%m.%d.%Y",
        "%Y %m %d",
        "%d %m %Y",
        "%m %d %Y",
    ]
    
    parsed_dates = []
    for date_str in date_strings:
        parsed = None
        for fmt in formats:
            try:
                parsed = datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        if parsed is None:
            raise ValueError(f"Unsupported date format: {date_str}")
        parsed_dates.append((parsed, date_str))
    
    parsed_dates.sort(key=lambda x: x[0])
    
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "15/01/2023",
        "01-15-2023",
        "2023/01/15",
        "15-01-2023",
        "01/15/2023",
        "2023.01.15",
        "15.01.2023",
        "01.15.2023",
        "2023 01 15",
        "15 01 2023",
        "01 15 2023",
        "2022-12-31",
        "31/12/2022",
        "12-31-2022",
        "2024-01-01",
        "01/01/2024",
        "2023-06-15",
        "15/06/2023",
        "06-15-2023",
    ]
    
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)