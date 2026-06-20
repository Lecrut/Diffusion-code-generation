from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        return datetime.strptime(date_str, DateDifferenceCalculator.DATE_FORMAT)

    @staticmethod
    def calculate_week_difference(date_str1: str, date_str2: str) -> int:
        date1 = DateDifferenceCalculator.parse_date(date_str1)
        date2 = DateDifferenceCalculator.parse_date(date_str2)
        difference_days = abs((date2 - date1).days)
        return difference_days // 7

if __name__ == '__main__':
    print(DateDifferenceCalculator.calculate_week_difference('2023-01-15', '2023-02-28'))
    print(DateDifferenceCalculator.calculate_week_difference('2023-02-28', '2023-01-15'))