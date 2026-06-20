from datetime import date

class DateDifference:
    def days_between_dates(self, date1: date, date2: date) -> int:
        return abs((date2 - date1).days)

if __name__ == '__main__':
    sample_date1 = date(2023, 8, 1)
    sample_date2 = date(2023, 8, 15)
    calculator = DateDifference()
    print(calculator.days_between_dates(sample_date1, sample_date2))