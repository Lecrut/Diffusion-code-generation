from datetime import datetime

class DateComparison:
    @staticmethod
    def parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> datetime:
        try:
            return datetime.strptime(date_string, date_format)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_string} with format {date_format}")

    def compare_dates(self, date1_str: str, date2_str: str) -> str:
        date1 = self.parse_date(date1_str)
        date2 = self.parse_date(date2_str)
        
        if date1 < date2:
            return "Date 1 is earlier"
        elif date1 > date2:
            return "Date 2 is earlier"
        else:
            return "Dates are equal"

if __name__ == '__main__':
    comparator = DateComparison()
    result = comparator.compare_dates("2023-04-01", "2023-05-01")
    print(result)