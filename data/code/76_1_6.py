import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"
    
    @staticmethod
    def _parse_date(date_str):
        return datetime.datetime.strptime(date_str, DateCalculator.DATE_FORMAT)
    
    def days_between(self, date1_str: str, date2_str: str) -> int:
        date1 = self._parse_date(date1_str)
        date2 = self._parse_date(date2_str)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.days_between("2023-01-01", "2023-01-15"))