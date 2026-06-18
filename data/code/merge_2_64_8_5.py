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
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.strftime("%A, %B %d, %Y")
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date string: {date_str}")
if __name__ == '__main__':
    test_cases = [
        "2023-10-05",
        "05/10/2023",
        "October 5, 2023",
        "Oct 5, 2023"
    ]
    for date in test_cases:
        result = parse_date(date)
        print(result)