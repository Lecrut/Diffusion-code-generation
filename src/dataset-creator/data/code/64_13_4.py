import datetime
from dateutil import parser as date_parser_lib
def parse_date_to_full_month(date_str: str) -> str:
    try:
        parsed = date_parser_lib.parse(date_str)
        return f"{parsed.month} {datestr}"
    except Exception:
        raise ValueError(f"Unable to parse date string: {date_str}")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "October 5, 2023",
        "05/10/2023",
        "Oct. 5th, '23"
    ]
    for date_str in sample_dates:
        try:
            result = parse_date_to_full_month(date_str)
            print(f"{date_str} -> {result}")
        except ValueError as e:
            print(f"Error processing '{date_str}': {e}")