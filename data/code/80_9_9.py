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
    def compare_dates(date1: datetime, date2: datetime, comparison_type: str = "less_than") -> str:
        if comparison_type == "less_than":
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
        elif comparison_type == "equal":
            if date1 == date2:
                return "date1 is equal to date2"
            else:
                return "date1 is not equal to date2"
        else:
            raise ValueError("Invalid comparison_type. Must be 'less_than', 'greater_than', or 'equal'.")
    @staticmethod
    def format_date(date_obj: datetime, date_format: str = "%Y-%m-%d") -> str:
        return date_obj.strftime(date_format)
if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-27"
    date_str3 = "2023-10-26"
    date_str_invalid = "26/10/2023"
    format_type = "%Y-%m-%d"
    date1 = DateUtils.parse_date(date_str1, format_type)
    date2 = DateUtils.parse_date(date_str2, format_type)
    date3 = DateUtils.parse_date(date_str3, format_type)
    date_invalid = DateUtils.parse_date(date_str_invalid, format_type)
    print(f"Parsing '{date_str1}': {date1}")
    print(f"Parsing '{date_str2}': {date2}")
    print(f"Parsing '{date_str3}': {date3}")
    print(f"Parsing '{date_str_invalid}': {date_invalid}")
    if date1 and date2:
        comparison_result = DateUtils.compare_dates(date1, date2, "less_than")
        print(f"\nComparing {date_str1} and {date_str2} (less_than): {comparison_result}")
        comparison_result_2 = DateUtils.compare_dates(date2, date1, "greater_than")
        print(f"Comparing {date_str2} and {date_str1} (greater_than): {comparison_result_2}")
        comparison_result_3 = DateUtils.compare_dates(date1, date3, "equal")
        print(f"Comparing {date_str1} and {date_str3} (equal): {comparison_result_3}")
    if date1 and date3:
        formatted_date1 = DateUtils.format_date(date1, "%m/%d/%Y")
        formatted_date3 = DateUtils.format_date(date3, "%m/%d/%Y")
        print(f"\nFormatting {date1} to MM/DD/YYYY: {formatted_date1}")
        print(f"Formatting {date3} to MM/DD/YYYY: {formatted_date3}")