from datetime import date

class YearDifferenceCalculator:
    MIN_DATE = date(1, 1, 1)
    MAX_DATE = date(9999, 12, 31)

    @staticmethod
    def _validate_date(d: date) -> date:
        if not isinstance(d, date):
            raise ValueError("Input must be a date object")
        if d < YearDifferenceCalculator.MIN_DATE or d > YearDifferenceCalculator.MAX_DATE:
            raise ValueError("Date out of valid range")
        return d

    @staticmethod
    def calculate(date1: date, date2: date) -> int:
        d1 = YearDifferenceCalculator._validate_date(date1)
        d2 = YearDifferenceCalculator._validate_date(date2)
        year_diff = abs(d1.year - d2.year)
        if (d1.month < d2.month) or (d1.month == d2.month and d1.day <= d2.day):
            if d1.year < d2.year:
                return year_diff - 1
            else:
                return year_diff + 1
        return year_diff

if __name__ == '__main__':
    start_date = date(2023, 10, 15)
    end_date = date(2010, 5, 20)
    diff = YearDifferenceCalculator.calculate(start_date, end_date)
    print(diff)