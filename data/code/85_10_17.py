from datetime import datetime

class DateCalculator:
    def get_week_diff(self, date1, date2):
        return abs((date2 - date1).days) // 7

if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = datetime(2023, 5, 1)
    date2 = datetime(2023, 6, 15)
    print(calculator.get_week_diff(date1, date2))