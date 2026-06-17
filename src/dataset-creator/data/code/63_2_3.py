import re
from datetime import date
class DateSubtractor:
    def _validate_date_string(self, s):
        if not isinstance(s, str) or len(s.strip()) == 0:
            raise ValueError("Date string must be a non-empty string.")
        pattern = r'^(\d{4})-(\d{2})-(\d{2})(T\d{2}:\d{2}:?\d{2}(?:.\d+)?)?$'
        match = re.match(pattern, s.strip())
        if not match:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD or ISO 8601.")
    def _parse_date(self, s):
        self._validate_date_string(s)
        try:
            dt_str = s.split('T')[0]
            year, month, day = map(int, dt_str.split('-'))
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid date components.")
        except ValueError:
            raise
        return date(year, month, day)
    def subtract_years(self, input_date_string, year_count=0):
        try:
            original_date = self._parse_date(input_date_string)
            if not isinstance(original_date, date):
                raise TypeError("Input must be a valid date string.")
            new_year = original_date.year - int(year_count)
            return date(new_year, original_date.month, original_date.day)
        except ValueError as e:
            raise ValueError(f"Invalid input provided: {e}") from None
if __name__ == '__main__':
    subtractor = DateSubtractor()
    test_cases = [
        ("2023-10-05", 1),
        ("1998-07-20", -10),
        ("2000-01-01", 0)
    ]
    for date_str, years in test_cases:
        try:
            result = subtractor.subtract_years(date_str, years)
            print(f"Subtracted {years} year(s) from {date_str}:")
            print(result.strftime("%Y-%m-%d"))
        except ValueError as e:
            print(f"Error processing '{date_str}' with offset {years}: {e}")