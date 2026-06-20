from datetime import datetime

class DateDifferenceCalculator:
    @staticmethod
    def get_days_between(date1, date2):
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 10)
    difference = calculator.get_days_between(date1, date2)
    print(difference)