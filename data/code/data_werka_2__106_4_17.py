from datetime import date

class DateCalculator:
    DAYS_PER_YEAR = 365

    @staticmethod
    def calculate_absolute_year_diff(d1: date, d2: date) -> int:
        if not isinstance(d1, date) or not isinstance(d2, date):
            raise ValueError("Inputs must be date objects")
        delta = d2 - d1
        total_days = abs(delta.days)
        return total_days // DateCalculator.DAYS_PER_YEAR

if __name__ == '__main__':
    start = date(2010, 5, 15)
    end = date(2023, 5, 15)
    diff = DateCalculator.calculate_absolute_year_diff(start, end)
    print(diff)