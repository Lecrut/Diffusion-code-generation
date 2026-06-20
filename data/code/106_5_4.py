from datetime import date

class DateDifferenceCalculator:
    def __init__(self, date1: date, date2: date):
        self.date1 = date1
        self.date2 = date2
    
    def calculate_year_difference(self) -> int:
        return abs((self.date2 - self.date1).days // 365)

if __name__ == '__main__':
    sample_date1 = date(1980, 7, 4)
    sample_date2 = date(2023, 10, 11)
    
    calculator = DateDifferenceCalculator(sample_date1, sample_date2)
    print(calculator.calculate_year_difference())