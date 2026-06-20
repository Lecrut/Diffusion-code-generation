import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    def days_between(self, date1_str: str, date2_str: str) -> int:
        date1 = self.parse_date(date1_str)
        date2 = self.parse_date(date2_str)
        return abs((date2 - date1).days)

    @staticmethod
    def parse_date(date_str: str) -> datetime.datetime:
        return datetime.datetime.strptime(date_str, DateCalculator.DATE_FORMAT)

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.days_between("2023-01-01", "2023-01-15")
    print(result)