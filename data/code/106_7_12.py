from datetime import date

class DateDifferenceCalculator:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date
    
    def is_before(self) -> bool:
        return (self.start_date.month, self.start_date.day) > (self.end_date.month, self.end_date.day)
    
    def calculate_years(self) -> int:
        year_diff = self.end_date.year - self.start_date.year
        if self.is_before():
            year_diff -= 1
        return year_diff

if __name__ == '__main__':
    start = date(2010, 5, 15)
    end = date(2023, 8, 20)
    calculator = DateDifferenceCalculator(start, end)
    print(calculator.calculate_years())