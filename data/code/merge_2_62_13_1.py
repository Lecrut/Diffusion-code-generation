import re
from datetime import datetime
class DateMonthCalculator:
    def _validate_date_string(self, date_str):
        if not isinstance(date_str, str) or len(date_str.strip()) == 0:
            raise ValueError("Date string must be a non-empty valid ISO 8601 format.")
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got '{date_str}'.")
    def _validate_month_delta(self, delta):
        if isinstance(delta, str) and (delta.strip() == '' or not re.match(r'^-?\d+$', delta)):
            raise ValueError("Month delta must be an integer.")
        try:
            return int(delta)
        except ValueError:
            raise ValueError(f"Invalid month delta value: '{delta}'.")
    def calculate(self, date_str, months):
        self._validate_date_string(date_str)
        self._validate_month_delta(months)
        parsed = datetime.strptime(date_str.strip(), "%Y-%m-%d")
        target_year = parsed.year + (months // 12)
        remaining_months = months % 12 if months >= 0 else -(abs(months) % 12)
        month_to_add = abs(remaining_months) - (1 if remaining_months < 0 and abs(remaining_months) > 0 else 0)
        target_month = parsed.month + int(month_to_add)
        while target_month <= 0 or target_month > 12:
            if target_month <= 0:
                target_year -= 1
                target_month += 12
            elif target_month > 12:
                target_year += 1
                target_month -= 12
        final_day = parsed.day
        try:
            new_date = datetime(target_year, target_month, final_day)
        except ValueError:
            if months >= 0 and remaining_months != 0:
                days_in_last_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if target_year % 4 == 0 and (target_year % 100 != 0 or target_year % 400 == 0):
                    days_in_last_month[1] = 29
                last_day_of_target_month = min(final_day, days_in_last_month[target.month - 1]) if months >= 0 else max(final_day, days_in_last_month[(target.month + remaining_months) % 12])
            new_date = datetime(target_year, target_month, final_day)
        return f"{new_date:%Y-%m-%d}"
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_cases = [
        ("2023-10-15", "6"),
        ("2024-02-28", "-3"),
        ("2023-01-31", "17"),
        ("2023-09-01", "1")
    ]
    for date_str, months in test_cases:
        try:
            result = calculator.calculate(date_str, months)
            print(f"Input Date: {date_str}, Delta Months: {months} -> Result: {result}")
        except Exception as e:
            print(f"Error processing '{date_str}' with delta {months}: {e}")