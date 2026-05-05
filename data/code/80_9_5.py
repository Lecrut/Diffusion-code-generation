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
    dt1 = DateComparator.parse_date(date_str1, format_type)
    dt2 = DateComparator.parse_date(date_str2, format_type)
    dt3 = DateComparator.parse_date(date_str3, format_type)
    print(f"Parsed Date 1: {dt1}")
    print(f"Parsed Date 2: {dt2}")
    print(f"Parsed Date 3: {dt3}\n")
    if dt1 and dt2:
        result1 = DateComparator.compare_dates(dt1, dt2, "less_than")
        print(f"Comparison (dt1 < dt2): {result1}")
        result2 = DateComparator.compare_dates(dt2, dt1, "greater_than")
        print(f"Comparison (dt2 > dt1): {result2}")
        result3 = DateComparator.compare_dates(dt1, dt3, "equal")
        print(f"Comparison (dt1 == dt3): {result3}\n")
    if dt2 and dt3:
        result4 = DateComparator.compare_dates(dt2, dt3, "equal")
        print(f"Comparison (dt2 == dt3): {result4}\n")
    if dt1:
        formatted_dt1 = DateComparator.format_date(dt1, "%m/%d/%Y")
        print(f"Formatted Date 1 (mm/dd/yyyy): {formatted_dt1}")