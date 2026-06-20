import datetime

class DateCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def parse_date(date_str):
        return datetime.datetime.strptime(date_str, DateCalculator.DATE_FORMAT).date()

    def calculate_difference(self, date1_str, date2_str):
        date1 = self.parse_date(date1_str)
        date2 = self.parse_date(date2_str)
        return abs(date2 - date1)

if __name__ == '__main__':
    calculator = DateCalculator()
    difference = calculator.calculate_difference('2023-01-01', '2023-01-15')
    print(difference.days)