from datetime import datetime
from typing import Optional
class DateComparisonError(Exception):
    pass
def parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> datetime:
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError as e:
        raise DateComparisonError(f"Error parsing date '{date_string}' with format '{date_format}': {e}")
def compare_dates(date1: datetime, date2: datetime, comparison_type: str = "equal") -> str:
    if comparison_type == "equal":
        if date1 == date2:
            return "equal"
        elif date1 < date2:
            return "date1 is before date2"
        else:
            return "date1 is after date2"
    elif comparison_type == "less_than":
        if date1 < date2:
            return "date1 is less than date2"
        elif date1 == date2:
            return "date1 is equal to date2"
        else:
            return "date1 is greater than date2"
    elif comparison_type == "greater_than":
        if date1 > date2:
            return "date1 is greater than date2"
        elif date1 == date2:
            return "date1 is equal to date2"
        else:
            return "date1 is less than date2"
    else:
        raise ValueError("Invalid comparison_type. Must be 'equal', 'less_than', or 'greater_than'.")
def format_date(date_obj: datetime, date_format: str = "%Y-%m-%d") -> str:
    return date_obj.strftime(date_format)
if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-26"
    date_str3 = "2023-10-27"
    date_str4 = "2023-10-25"
    try:
        date1 = parse_date(date_str1)
        date2 = parse_date(date_str2)
        date3 = parse_date(date_str3)
        date4 = parse_date(date_str4)
        print(f"Date 1: {date1}")
        print(f"Date 2: {date2}")
        print(f"Date 3: {date3}")
        print(f"Date 4: {date4}\n")
        print("--- Comparison Tests (Equal) ---")
        result1 = compare_dates(date1, date2, "equal")
        print(f"Comparing {date1} and {date2} (equal): {result1}")
        result2 = compare_dates(date1, date3, "equal")
        print(f"Comparing {date1} and {date3} (equal): {result2}")
        print("\n--- Comparison Tests (Less Than) ---")
        result3 = compare_dates(date1, date4, "less_than")
        print(f"Comparing {date1} and {date4} (less_than): {result3}")
        result4 = compare_dates(date3, date1, "less_than")
        print(f"Comparing {date3} and {date1} (less_than): {result4}")
        print("\n--- Comparison Tests (Greater Than) ---")
        result5 = compare_dates(date3, date1, "greater_than")
        print(f"Comparing {date3} and {date1} (greater_than): {result5}")
        print("\n--- Formatting Tests ---")
        formatted1 = format_date(date1, "%m/%d/%Y")
        formatted3 = format_date(date3, "%m/%d/%Y")
        print(f"Date 1 formatted as MM/DD/YYYY: {formatted1}")
        print(f"Date 3 formatted as MM/DD/YYYY: {formatted3}")
    except DateComparisonError as e:
        print(f"An error occurred: {e}")
    except ValueError as e:
        print(f"A value error occurred: {e}")