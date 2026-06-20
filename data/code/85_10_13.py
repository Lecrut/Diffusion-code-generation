from datetime import datetime

class DateCalculator:
    def get_week_diff(self, date1, date2):
        delta = abs(date1 - date2)
        return delta.days // 7

if __name__ == '__main__':
    calc = DateCalculator()
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 15)
    print(calc.get_week_diff(date1, date2))