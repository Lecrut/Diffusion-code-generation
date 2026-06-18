import datetime
from dateutil import parser as date_parser
def convert_date_to_full_month(date_str: str) -> str:
    try:
        parsed_dt = date_parser.parse(date_str)
        return parsed_dt.strftime("%B %d, %Y")
    except Exception:
        raise ValueError(f"Unable to parse date string: {date_str}")
if __name__ == '__main__':
    sample_dates = [
        "01/15/2023",
        "January 1st, 2024",
        "2023-12-25T10:30:00",
        "Dec. 31, 2022"
    ]
    for date_input in sample_dates:
        result = convert_date_to_full_month(date_input)
        print(f"{date_input} -> {result}")