from datetime import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def get_difference(date1, date2):
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = datetime.strptime("2023-01-01", calculator.DATE_FORMAT)
    date2 = datetime.strptime("2023-01-10", calculator.DATE_FORMAT)
    difference = calculator.get_difference(date1, date2)
    print(difference)