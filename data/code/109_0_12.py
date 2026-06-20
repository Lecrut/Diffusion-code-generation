import datetime

class MonthDaysCalculator:
    def __init__(self):
        self.current_date = datetime.date.today()
    
    @staticmethod
    def days_in_month(year, month):
        if month == 12:
            return (datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)).days
        else:
            return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    
    def days_remaining_in_current_month(self):
        current_year = self.current_date.year
        current_month = self.current_date.month
        return self.days_in_month(current_year, current_month) - (self.current_date.day - 1)

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    print(calculator.days_remaining_in_current_month())