import datetime

class DateDifferenceCalculator:

    def __init__(self):
        self.formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y', '%Y/%m/%d']

    def parse_date(self, date_string):
        for fmt in self.formats:
            try:
                return datetime.datetime.strptime(date_string, fmt).date()
            except ValueError:
                continue
        raise ValueError('Invalid date format')

    def calculate_difference(self, date_str1, date_str2):
        date1 = self.parse_date(date_str1)
        date2 = self.parse_date(date_str2)
        return abs((date1 - date2).days)
if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result = calculator.calculate_difference('2023-10-05', '10/07/2023')
    print(result)