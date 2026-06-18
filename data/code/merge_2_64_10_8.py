import datetime
from dateutil import parser as date_parser
def convert_date_to_full_string(date_str: str) -> str:
    try:
        parsed_date = date_parser.parse(date_str, dayfirst=False)
        return parsed_date.strftime("%B %d, %Y")
    except Exception as e:
        raise ValueError(f"Invalid date format or parsing error: {e}")
if __name__ == '__main__':
    sample_dates = [
        "01/15/2023",
        "January 15, 2023",
        "2023-01-15T14:30:00",
        "15-Jan-2023"
    ]
    for date_str in sample_dates:
        try:
            result = convert_date_to_full_string(date_str)
            print(f"{date_str} -> {result}")
        except ValueError as ve:
            print(f"Error processing '{date_str}': {ve}")