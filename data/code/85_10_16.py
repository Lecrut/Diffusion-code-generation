from datetime import datetime

class DateCalculator:
    def get_week_diff(self, date1, date2):
        delta = abs(date2 - date1)
        return delta.days // 7

if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = datetime(2023, 4, 1)
    date2 = datetime(2023, 6, 15)
    print(calculator.get_week_diff(date1, date2))