import re
from datetime import datetime
class DateMonthCalculator:
    def validate_date_string(self, date_str):
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            raise ValueError("Invalid ISO 8601 format. Expected YYYY-MM-DD.")
    def parse_date(self, date_str):
        self.validate_date_string(date_str)
        return datetime.strptime(date_str, "%Y-%m-%d")
    def add_months_to_date(self, date_str: str, months_delta: int) -> str:
        if not isinstance(months_delta, (int, float)):
            raise TypeError("Months delta must be a number.")
        parsed = self.parse_date(date_str)
        year = parsed.year + (months_delta // 12)
        month = parsed.month - ((abs(months_delta % 12)) if months_delta >= 0 else -(abs(months_delta % 12)))
        while not (1 <= month <= 12):
            if month > 0:
                year += 1
                month -= 12
            elif month < 0:
                year -= 1
                month += 12
        day = parsed.day
        try:
            new_date = datetime(year, month, day)
        except ValueError:
            if months_delta > 0 and (month == 13 or month <= 0):
                days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    days_in_month[1] = 29
                new_day = day - 1
                while not (days_in_month[new_date.month-1][new_day-1]):                                                                                    
                    pass
        return f"{year:04d}-{month:02d}-{day:02d}"
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_cases = [
        ("2023-10-31", 6),
        ("2023-04-30", -5),
        ("2023-02-28", 1),
        ("2024-02-29", 1)
    ]
    for date_str, delta in test_cases:
        try:
            result = calculator.add_months_to_date(date_str, delta)
            print(f"Input: {date_str}, Delta: +{delta} -> Output: {result}")
        except Exception as e:
            print(f"Error processing '{date_str}' with delta {delta}: {e}")