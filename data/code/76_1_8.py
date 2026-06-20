import datetime

class DateCalculator:
    def days_between(self, date1_str: str, date2_str: str) -> int:
        try:
            date_format = "%Y-%m-%d"
            date1 = datetime.datetime.strptime(date1_str, date_format)
            date2 = datetime.datetime.strptime(date2_str, date_format)
            return abs((date2 - date1).days)
        except ValueError as e:
            print(f"Invalid date format: {e}")
            return None

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.days_between("2023-01-01", "2023-01-15")
    print(result)