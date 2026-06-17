import re
from datetime import datetime
def parse_date(date_string):
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "dd/mm/yyyy",
        "%d/%m/%Y",
        "%b %d, %Y"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_string.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date string: {date_string}")
def format_date_with_full_month(dt):
    return dt.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "October 5, 2023",
        "05/10/2023",
        "Oct 5, 2023"
    ]
    for date_str in sample_dates:
        try:
            parsed = parse_date(date_str)
            result = format_date_with_full_month(parsed)
            print(f"Input: {date_str} -> Output: {result}")
        except ValueError as e:
            print(f"Error parsing '{date_str}': {e}")