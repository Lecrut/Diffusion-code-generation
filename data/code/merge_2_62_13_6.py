import datetime
class DateMonthCalculator:
    def add_months(self, date_str: str, months_delta: int) -> str:
        if not isinstance(date_str, str):
            raise TypeError("Date string must be provided.")
        try:
            parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error: {e}") from e
        if not isinstance(months_delta, int):
            raise TypeError("Month delta must be an integer.")
        try:
            new_date = parsed_date + datetime.timedelta(days=30 * months_delta)
        except OverflowError:
            raise ValueError(f"Date overflow occurred when adding {months_delta} months to {date_str}.") from None
        return new_date.strftime("%Y-%m-%d")
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_cases = [
        ("2023-10-05", 6),
        ("2024-02-28", -3),
        ("2020-07-15", 12)
    ]
    for date_input, month_change in test_cases:
        try:
            result = calculator.add_months(date_input, month_change)
            print(f"Input: {date_input}, Delta: +{month_change} -> Output (ISO): {result}")
        except Exception as e:
            print(f"Error processing '{date_input}' with delta {month_change}: {e}")