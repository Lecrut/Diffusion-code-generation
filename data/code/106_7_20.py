from datetime import date

class DateDifferenceCalculator:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date
    
    @staticmethod
    def is_before(start: date, end: date) -> bool:
        return start > end
    
    def calculate_years(self) -> int:
        if self.is_before(self.start_date, self.end_date):
            raise ValueError("Start date must be before end date.")
        
        year_diff = self.end_date.year - self.start_date.year
        month_day_diff = (self.end_date.month, self.end_date.day) < (self.start_date.month, self.start_date.day)
        
        return year_diff - month_day_diff

if __name__ == '__main__':
    start = date(2010, 5, 15)
    end = date(2023, 8, 20)
    calculator = DateDifferenceCalculator(start, end)
    print(calculator.calculate_years())