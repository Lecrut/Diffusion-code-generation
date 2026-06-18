import datetime
from dateutil import parser as datetool_parser
def parse_date_to_full_month(date_string: str) -> str:
    try:
        parsed = datetool_parser.parse(date_string)
        return f"{parsed.strftime('%B')}, {parsed.year}"
    except ValueError:
        raise ValueError(f"Unable to parse date string '{date_string}'.")
if __name__ == '__main__':
    sample_dates = [
        "01/23/2024",
        "January 5, 2024",
        "2024-06-15T10:30:00",
        "May 19, 2024"
    ]
    for date_str in sample_dates:
        print(parse_date_to_full_month(date_str))