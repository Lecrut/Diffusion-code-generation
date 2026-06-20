from datetime import datetime

class DateCalculator:
    def __init__(self, date_str1, date_str2):
        self.date_format = '%Y-%m-%d'
        try:
            self.date1 = datetime.strptime(date_str1, self.date_format)
            self.date2 = datetime.strptime(date_str2, self.date_format)
        except TypeError as e:
            print(f'TypeError: {e}')
            raise

    def calculate_days(self):
        delta = abs((self.date2 - self.date1).days)
        return delta

if __name__ == '__main__':
    calculator = DateCalculator('2023-01-01', '2023-01-31')
    result = calculator.calculate_days()
    print(result)