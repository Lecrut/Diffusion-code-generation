from datetime import datetime
from typing import Optional
class DateUtils:
    @staticmethod
    def parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> Optional[datetime]:
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            return None
    @staticmethod
    def compare_dates(date1: datetime, date2: datetime, operation: str) -> bool:
        if operation == "greater_than":
            return date1 > date2
        elif operation == "less_than":
            return date1 < date2
        elif operation == "equal_to":
            return date1 == date2
        else:
            raise ValueError("Invalid comparison operation. Must be 'greater_than', 'less_than', or 'equal_to'.")
    @staticmethod
    def format_date(date_obj: datetime, date_format: str = "%Y-%m-%d") -> str:
        return date_obj.strftime(date_format)
if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-25"
    date_str3 = "2023-10-26"
    date_str_invalid = "26/10/2023"
    format_type = "%Y-%m-%d"
    date1 = DateUtils.parse_date(date_str1, format_type)
    date2 = DateUtils.parse_date(date_str2, format_type)
    date3 = DateUtils.parse_date(date_str3, format_type)
    date_invalid = DateUtils.parse_date(date_str_invalid, format_type)
    print(f"Date 1 parsed: {date1}")
    print(f"Date 2 parsed: {date2}")
    print(f"Date 3 parsed: {date3}")
    print(f"Invalid date parsed: {date_invalid}")
    if date1 and date2:
        print("\n--- Comparison ---")
        print(f"Is Date 1 greater than Date 2? {DateUtils.compare_dates(date1, date2, 'greater_than')}")
        print(f"Is Date 1 less than Date 2? {DateUtils.compare_dates(date1, date2, 'less_than')}")
        print(f"Are Date 1 and Date 3 equal? {DateUtils.compare_dates(date1, date3, 'equal_to')}")
    if date1:
        print("\n--- Formatting ---")
        formatted1 = DateUtils.format_date(date1, "%m/%d/%Y")
        formatted2 = DateUtils.format_date(date2, "%m/%d/%Y")
        print(f"Date 1 formatted as MM/DD/YYYY: {formatted1}")
        print(f"Date 2 formatted as MM/DD/YYYY: {formatted2}")