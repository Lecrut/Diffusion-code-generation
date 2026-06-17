import re
from datetime import datetime
def parse_date(date_str):
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "January 15, 2023"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date string: {date_str}")
def format_date_with_full_month(dt):
    return dt.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "05/10/2023",
        "October 5, 2023",
        "Oct 5, 2023"
    ]
    for date_str in sample_dates:
        try:
            parsed = parse_date(date_str)
            result = format_date_with_full_month(parsed)
            print(f"Input: {date_str} -> Output: {result}")
        except ValueError as e:
            print(f"Error processing '{date_str}': {e}")