from datetime import datetime
from typing import Union
def parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> datetime:
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_string}' with format '{date_format}': {e}")
def compare_dates(date1: datetime, date2: datetime) -> int:
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0
def format_date(date_obj: datetime, date_format: str = "%Y-%m-%d") -> str:
    return date_obj.strftime(date_format)
if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-25"
    date_str3 = "2024-01-01"
    date_format_input = "%Y-%m-%d"
    try:
        date1 = parse_date(date_str1, date_format_input)
        date2 = parse_date(date_str2, date_format_input)
        date3 = parse_date(date_str3, date_format_input)
        comparison_result = compare_dates(date1, date2)
        print(f"Comparison between {date_str1} and {date_str2}: {comparison_result}")
        comparison_result_2 = compare_dates(date3, date1)
        print(f"Comparison between {date_str3} and {date_str1}: {comparison_result_2}")
        formatted_date1 = format_date(date1, "%m/%d/%Y")
        print(f"Formatted {date1} as MM/DD/YYYY: {formatted_date1}")
        formatted_date3 = format_date(date3, "%d-%b-%Y")
        print(f"Formatted {date3} as DD-Mon-YYYY: {formatted_date3}")
    except ValueError as e:
        print(f"An error occurred: {e}")