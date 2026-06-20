from datetime import datetime

class DateCalculator:
    @staticmethod
    def is_valid_date(date):
        return isinstance(date, datetime)

    def get_week_diff(self, date1, date2):
        if not (self.is_valid_date(date1) and self.is_valid_date(date2)):
            raise ValueError("Both inputs must be datetime objects.")
        
        delta = abs(date2 - date1)
        return delta.days // 7

if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 2, 5)
    print(calculator.get_week_diff(date1, date2))