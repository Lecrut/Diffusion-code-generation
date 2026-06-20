from datetime import date

class DateCalculator:
    DAYS_PER_YEAR = 365
    
    @staticmethod
    def get_difference(date1: date, date2: date) -> int:
        return abs((date2 - date1).days // DateCalculator.DAYS_PER_YEAR)

if __name__ == '__main__':
    calculator = DateCalculator()
    d1 = date(2010, 1, 1)
    d2 = date(2023, 4, 15)
    difference = calculator.get_difference(d1, d2)
    print(difference)