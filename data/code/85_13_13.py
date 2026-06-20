from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def calculate_week_difference(date_str1: str, date_str2: str) -> int:
        try:
            date1 = datetime.strptime(date_str1, DateDifferenceCalculator.DATE_FORMAT)
            date2 = datetime.strptime(date_str2, DateDifferenceCalculator.DATE_FORMAT)
            difference = abs((date2 - date1).days)
            weeks = difference // 7
            return weeks
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_week_difference('2023-01-01', '2023-01-15'))
    print(calculator.calculate_week_difference('2023-02-28', '2023-03-29'))