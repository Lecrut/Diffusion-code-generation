import re
from datetime import datetime
class DateMonthCalculator:
    def validate_date_string(self, date_str):
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            raise ValueError("Invalid ISO 8601 format. Expected YYYY-MM-DD.")
    def parse_date_to_object(self, date_str):
        self.validate_date_string(date_str)
        return datetime.strptime(date_str, "%Y-%m-%d")
    def add_months(self, date_obj: datetime, months_delta: int) -> str:
        if not isinstance(months_delta, (int, float)):
            raise TypeError("Months delta must be a number.")
        year = date_obj.year + ((months_delta // 12))
        month = date_obj.month - abs((abs(months_delta) % 12))
        while month < 1:
            month += 12
            year -= 1
        day = min(date_obj.day, (datetime(year, month, 0).day))
        return f"{year}-{month:02d}-{date_obj.day:02d}"
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_cases = [
        ("2023-10-15", 6),
        ("2024-02-28", -3),
        ("2023-01-31", 1)
    ]
    for date_str, months in test_cases:
        try:
            result = calculator.add_months(calculator.parse_date_to_object(date_str), int(months))
            print(f"Input: {date_str}, Delta: +{months} -> Output: {result}")
        except Exception as e:
            print(f"Error processing {date_str}: {e}")