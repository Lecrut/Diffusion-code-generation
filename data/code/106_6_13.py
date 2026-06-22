from datetime import datetime

class DateDiffCalculator:
    DATE_FORMAT = "%Y-%m-%d"
    SEPARATOR = "-"

    @staticmethod
    def parse_date(date_string: str) -> datetime:
        try:
            return datetime.strptime(date_string, DateDiffCalculator.DATE_FORMAT)
        except ValueError as e:
            raise ValueError(f"Date '{date_string}' is not valid. Expected format: YYYY-MM-DD") from e

    @classmethod
    def compute_year_difference(cls, start_date_str: str, end_date_str: str) -> int:
        start_dt = cls.parse_date(start_date_str)
        end_dt = cls.parse_date(end_date_str)
        
        year_diff = end_dt.year - start_dt.year
        
        if (end_dt.month, end_dt.day) < (start_dt.month, start_dt.day):
            year_diff -= 1
            
        return year_diff

if __name__ == '__main__':
    start = "2020-02-29"
    end = "2024-03-01"
    difference = DateDiffCalculator.compute_year_difference(start, end)
    print(difference)