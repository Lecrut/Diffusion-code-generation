import re
from datetime import datetime
class DateMonthCalculator:
    def add_months(self, date_str: str, months_delta: int) -> str:
        if not isinstance(date_str, str):
            raise TypeError("Date string must be provided.")
        pattern = r'^(\d{4})-(\d{2})-(\d{2})(T\d{2}:\d{2}(?::\d{2})?)?$'
        match = re.match(pattern, date_str.strip())
        if not match:
            raise ValueError("Invalid ISO 8601 format.")
        try:
            year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
            time_str = match.group(4) or "T" + f"{match.group(5)}:{match.group(6)}:00".replace(":", "")[:8] if len(time_str) > 2 else ""
        except ValueError:
            raise ValueError(f"Invalid date components in '{date_str}'.")
        try:
            new_month = (month - 1 + months_delta) % 12 + 1
            new_year = year + ((months_delta // 12)) if months_delta > 0 else year - abs(months_delta // 12)
        except Exception:
            raise ValueError("Invalid calendar adjustment.")
        try:
            base_date = f"{new_year}-{int(new_month):02d}-1"
            target_date = datetime.strptime(base_date, "%Y-%m-%d") + timedelta(days=days_in_month[new_month][target_date.month]) - timedelta(days=(datetime(target_date.year, new_month, 1).day))
        except Exception:
            raise ValueError("Invalid date calculation.")
        return f"{new_year}-{int(new_month):02d}-{int(day):02d}"
def days_in_month(year: int, month: int) -> int:
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return 29 if is_leap else 28
    else:
        return 31
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_cases = [
        ("2023-05-15", 6),
        ("2024-02-29", -3),
        ("2023-07-31", 1),
        ("invalid-date", 1)
    ]
    for date_input, months in test_cases:
        try:
            result = calculator.add_months(date_input, months)
            print(f"Input: {date_input}, Delta: +{months} -> Output (ISO): {result}")
        except Exception as e:
            print(f"Error processing '{date_input}': {e}")