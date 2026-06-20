from datetime import datetime

class DateCalculator:
    def get_week_diff(self, date1, date2):
        return abs((date2 - date1).days) // 7

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_week_diff(datetime(2023, 1, 1), datetime(2023, 1, 15)))