from datetime import datetime
from typing import Optional
class DateComparator:
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
    date_str1 = "2023-10-25"
    date_str2 = "2023-11-15"
    date_str3 = "2023-10-25"
    format_type = "%Y-%m-%d"
    date1 = DateComparator.parse_date(date_str1, format_type)
    date2 = DateComparator.parse_date(date_str2, format_type)
    date3 = DateComparator.parse_date(date_str3, format_type)
    print(f"Parsed Date 1: {date1}")
    print(f"Parsed Date 2: {date2}")
    print(f"Parsed Date 3: {date3}")
    if date1 and date2:
        comparison_result = DateComparator.compare_dates(date1, date2, "less_than")
        print(f"\nComparison (Date1 < Date2): {comparison_result}")
        comparison_result_2 = DateComparator.compare_dates(date2, date1, "greater_than")
        print(f"Comparison (Date2 > Date1): {comparison_result_2}")
        comparison_result_3 = DateComparator.compare_dates(date1, date3, "equal")
        print(f"Comparison (Date1 == Date3): {comparison_result_3}")
    if date1 and date3:
        comparison_result_4 = DateComparator.compare_dates(date1, date3, "equal")
        print(f"Comparison (Date1 == Date3): {comparison_result_4}")
    if date1:
        formatted_date1 = DateComparator.format_date(date1, "%m/%d/%Y")
        print(f"\nFormatted Date 1 (MM/DD/YYYY): {formatted_date1}")