from datetime import date

class DateCalculator:
    @staticmethod
    def days_between_dates(date1: date, date2: date) -> int:
        return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 15)
    print(DateCalculator.days_between_dates(date1, date2))