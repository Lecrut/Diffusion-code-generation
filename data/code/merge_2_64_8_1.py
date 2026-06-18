import re
from datetime import datetime
def parse_date(date_str):
    patterns = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "January 15, 2023",
        "Jan 15, 2023"
    ]
    for pattern in patterns:
        try:
            return datetime.strptime(date_str.strip(), pattern)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date string: {date_str}")
def format_date_with_month_name(dt):
    return dt.strftime("%B %d, %Y")
if __name__ == '__main__':
    samples = [
        "2023-15-04",                                                                   
        "15/04/2023",
        "April 15, 2023",
        "Apr 15, 2023"
    ]
    for sample in samples:
        try:
            parsed = parse_date(sample)
            result = format_date_with_month_name(parsed)
            print(f"Input: {sample} -> Output: {result}")
        except ValueError as e:
            print(f"Error processing '{sample}': {e}")