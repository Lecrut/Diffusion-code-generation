from datetime import datetime

class DateCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def calculate_days(date_str1, date_str2):
        try:
            date1 = datetime.strptime(date_str1, DateCalculator.DATE_FORMAT)
            date2 = datetime.strptime(date_str2, DateCalculator.DATE_FORMAT)
            delta = abs((date2 - date1).days)
            return delta
        except TypeError as e:
            print(f'TypeError: {e}')
            return None

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_days('2023-01-01', '2023-01-31')
    print(result)