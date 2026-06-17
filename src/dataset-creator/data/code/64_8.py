import re
from datetime import datetime
def parse_date(date_str):
    patterns = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y"
    ]
    for pattern in patterns:
        try:
            return datetime.strptime(date_str.strip(), pattern)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date string: {date_str}")
def format_date_with_full_month(dt):
    return dt.strftime("%B %d, %Y")
if __name__ == '__main__':
    samples = [
        "2023-10-05",
        "05/10/2023",
        "October 5, 2023",
        "Oct 5, 2023"
    ]
    for sample in samples:
        try:
            dt = parse_date(sample)
            result = format_date_with_full_month(dt)
            print(f"{sample} -> {result}")
        except ValueError as e:
            print(f"Error parsing '{sample}': {e}")