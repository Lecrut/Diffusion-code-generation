from datetime import datetime

class YearDifferenceCalculator:
    _DATE_FORMAT = "%Y-%m-%d"
    _YEAR_THRESHOLD = 365.2425

    @staticmethod
    def _parse_date(date_string: str) -> datetime:
        try:
            return datetime.strptime(date_string, YearDifferenceCalculator._DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_string}. Expected YYYY-MM-DD.")

    @staticmethod
    def calculate_years(date1_str: str, date2_str: str) -> float:
        date1 = YearDifferenceCalculator._parse_date(date1_str)
        date2 = YearDifferenceCalculator._parse_date(date2_str)
        delta = abs(date2 - date1)
        days = delta.days
        hours = delta.seconds / 3600.0
        total_days = days + hours
        return total_days / YearDifferenceCalculator._YEAR_THRESHOLD

if __name__ == '__main__':
    start_date = "2015-06-15"
    end_date = "2023-06-15"
    difference = YearDifferenceCalculator.calculate_years(start_date, end_date)
    print(difference)