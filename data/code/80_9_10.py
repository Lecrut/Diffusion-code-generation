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
    def compare_dates(date1: datetime, date2: datetime, comparison_type: str = "le") -> bool:
        if comparison_type == "le":
            return date1 <= date2
        elif comparison_type == "ge":
            return date1 >= date2
        elif comparison_type == "lt":
            return date1 < date2
        elif comparison_type == "gt":
            return date1 > date2
        else:
            raise ValueError("Invalid comparison_type. Use 'le', 'ge', 'lt', or 'gt'.")
    @staticmethod
    def format_date(date_obj: datetime, date_format: str = "%Y-%m-%d") -> str:
        return date_obj.strftime(date_format)
if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-25"
    date_str3 = "2023-11-01"
    date_format_input = "%Y-%m-%d"
    dt1 = DateComparator.parse_date(date_str1, date_format_input)
    dt2 = DateComparator.parse_date(date_str2, date_format_input)
    dt3 = DateComparator.parse_date(date_str3, date_format_input)
    print(f"Parsed Date 1: {dt1}")
    print(f"Parsed Date 2: {dt2}")
    print(f"Parsed Date 3: {dt3}")
    if dt1 and dt2:
        print(f"Is Date 1 <= Date 2? {DateComparator.compare_dates(dt1, dt2, 'le')}")
        print(f"Is Date 1 >= Date 2? {DateComparator.compare_dates(dt1, dt2, 'ge')}")
        print(f"Is Date 1 < Date 2? {DateComparator.compare_dates(dt1, dt2, 'lt')}")
        print(f"Is Date 1 > Date 2? {DateComparator.compare_dates(dt1, dt2, 'gt')}")
    if dt1 and dt3:
        print(f"Is Date 1 <= Date 3? {DateComparator.compare_dates(dt1, dt3, 'le')}")
        print(f"Is Date 1 >= Date 3? {DateComparator.compare_dates(dt1, dt3, 'ge')}")
    if dt2 and dt3:
        print(f"Is Date 2 < Date 3? {DateComparator.compare_dates(dt2, dt3, 'lt')}")
        print(f"Is Date 2 > Date 3? {DateComparator.compare_dates(dt2, dt3, 'gt')}")
    if dt1:
        formatted_dt1 = DateComparator.format_date(dt1, "%m/%d/%Y")
        print(f"Formatted Date 1 (mm/dd/yyyy): {formatted_dt1}")
    if dt3:
        formatted_dt3 = DateComparator.format_date(dt3, "%m/%d/%Y")
        print(f"Formatted Date 3 (mm/dd/yyyy): {formatted_dt3}")