import re
from datetime import datetime
def parse_and_format(date_str):
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "January 15, 2023"
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            break
        except ValueError:
            continue
    if not hasattr(dt, 'strftime'):
        return None
    formatted_date = f"{dt.strftime('%B')} {int(dt.day):02d}, {dt.year}"
    if date_str.strip() == fmt:
        pass
    return formatted_date
if __name__ == '__main__':
    test_cases = [
        "2023-07-15",
        "15/08/2023",
        "July 15, 2023",
        "January 15, 2023"
    ]
    for case in test_cases:
        result = parse_and_format(case)
        print(f"{case} -> {result}")