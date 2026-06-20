from datetime import datetime

class DateCalculator:
    WEEKS_TO_DAYS = 7
    
    def get_week_diff(self, date1, date2):
        delta = abs(date2 - date1)
        return delta.days // self.WEEKS_TO_DAYS

if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 15)
    print(calculator.get_week_diff(date1, date2))