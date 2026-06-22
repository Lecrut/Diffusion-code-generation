from datetime import datetime

class YearCalculator:
    def __init__(self, start_year: int, start_month: int, start_day: int):
        self.start_date = datetime(start_year, start_month, start_day)

    def calculate(self, end_year: int, end_month: int, end_day: int) -> int:
        end_date = datetime(end_year, end_month, end_day)
        if end_date < self.start_date:
            raise ValueError("End date must be greater than or equal to start date")
        
        years = end_date.year - self.start_date.year
        if end_date.month < self.start_date.month or (
            end_date.month == self.start_date.month and end_date.day < self.start_date.day
        ):
            years -= 1
        return years

if __name__ == '__main__':
    calculator = YearCalculator(2000, 2, 29)
    result1 = calculator.calculate(2023, 2, 28)
    print(result1)
    
    result2 = calculator.calculate(2024, 2, 29)
    print(result2)
    
    calculator2 = YearCalculator(1990, 1, 1)
    result3 = calculator2.calculate(2023, 12, 31)
    print(result3)