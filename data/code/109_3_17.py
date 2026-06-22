import calendar
from datetime import datetime

class MonthCalculator:
    DAYS_IN_WEEK = 7
    MONTHS_IN_YEAR = 12

    @staticmethod
    def get_days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def is_leap_year(year):
        return calendar.isleap(year)

    def calculate_days_left(self, year, month, day):
        if not (1 <= month <= self.MONTHS_IN_YEAR):
            raise ValueError("Invalid month")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day")
        
        total_days = self.get_days_in_month(year, month)
        if day > total_days:
            raise ValueError("Day out of range for month")
        
        return total_days - day

if __name__ == '__main__':
    calculator = MonthCalculator()
    now = datetime.now()
    days_left = calculator.calculate_days_left(now.year, now.month, now.day)
    print(days_left)