from datetime import date

class DateCalculator:
    MIN_DATE = date(1900, 1, 1)
    MAX_DATE = date(2100, 12, 31)

    @staticmethod
    def days_between_dates(date1: date, date2: date) -> int:
        if not (DateCalculator.MIN_DATE <= date1 <= DateCalculator.MAX_DATE and 
                DateCalculator.MIN_DATE <= date2 <= DateCalculator.MAX_DATE):
            raise ValueError("Dates must be between 1900-01-01 and 2100-12-31")
        delta = abs(date2 - date1)
        return delta.days

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2023, 12, 31)
    print(DateCalculator.days_between_dates(sample_date1, sample_date2))