import datetime
from dateutil import parser
def parse_date_to_full_month(date_str):
    try:
        parsed = parser.parse(date_str)
        return f"{parsed.month} {parsed.day}"
    except Exception as e:
        raise ValueError(f"Invalid date format or parsing error: {e}")
if __name__ == '__main__':
    test_dates = [
        "01/15/2023",
        "January 15, 2023",
        "15-Jan-2023",
        "2023.01.15"
    ]
    for date_str in test_dates:
        result = parse_date_to_full_month(date_str)
        print(f"{date_str} -> {result}")