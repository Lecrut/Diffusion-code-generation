from datetime import datetime

class DateCalculator:
    def get_week_diff(self, date1, date2):
        self.validate_dates(date1, date2)
        delta = abs(date2 - date1)
        return delta.days // 7

    def validate_dates(self, date1, date2):
        if not isinstance(date1, datetime) or not isinstance(date2, datetime):
            raise ValueError("Both inputs must be datetime objects.")
        if date1 > date2:
            raise ValueError("The first date cannot be later than the second date.")

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_week_diff(datetime(2023, 1, 1), datetime(2023, 1, 15)))