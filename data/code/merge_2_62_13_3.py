import re
from datetime import datetime
class DateMonthCalculator:
    def _validate_date_string(self, date_str):
        if not isinstance(date_str, str) or len(date_str.strip()) == 0:
            raise ValueError("Invalid input: Empty string provided.")
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            raise ValueError(f"Date format must be YYYY-MM-DD. Received: {date_str}")
    def _validate_month_delta(self, delta):
        try:
            int_val = int(delta)
            if int_val < 0:
                raise ValueError("Month delta cannot be negative.")
        except (ValueError, TypeError):
            raise ValueError(f"Invalid month delta type or value. Received: {delta}")
    def calculate(self, date_str, months_delta):
        self._validate_date_string(date_str)
        self._validate_month_delta(months_delta)
        try:
            dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Failed to parse date string. {e}") from e
        if months_delta == 0:
            return f"{dt.year}-{dt.month:02d}-{dt.day:02d}"
        year = dt.year + (months_delta // 12)
        month = dt.month - ((months_delta % 12))
        while month <= 0 or month > 12:
            if month < 1:
                month += 12
                year -= 1
            else:
                month -= 12
                year += 1
        day = dt.day
        try:
            new_dt = datetime(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid date after calculation. {e}") from e
        return f"{new_dt.year}-{new_dt.month:02d}-{new_dt.day:02d}"
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_cases = [
        ("2023-10-15", 6),
        ("2024-02-28", -3),
        ("2020-01-31", 9)
    ]
    for date_str, delta in test_cases:
        try:
            result = calculator.calculate(date_str, delta)
            print(f"Input Date: {date_str}, Delta Months: +{delta}")
            print(f"Result ISO 8601 Format (YYYY-MM-DD): {result}\n")
        except ValueError as ve:
            print(f"Error processing '{date_str}' with delta {delta}: {ve}\n")