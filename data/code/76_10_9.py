from datetime import datetime

class DateCalculator:

    def get_difference(self, date1_str: str, date2_str: str) -> int:
        try:
            date1 = self.validate_date(date1_str)
            date2 = self.validate_date(date2_str)
            diff = abs((date1 - date2).days)
            return diff
        except ValueError:
            return -1

    def validate_date(self, date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Invalid date format. Please use YYYY-MM-DD.')
if __name__ == '__main__':
    calculator = DateCalculator()
    result1 = calculator.get_difference('2023-01-01', '2023-01-10')
    print(result1)
    result2 = calculator.get_difference('2024-12-31', '2025-01-01')
    print(result2)