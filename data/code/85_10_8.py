from datetime import datetime

class DateCalculator:
    @staticmethod
    def get_week_diff(date1, date2):
        delta = abs((date2 - date1).days)
        return delta // 7

if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 15)
    print(calculator.get_week_diff(date1, date2))