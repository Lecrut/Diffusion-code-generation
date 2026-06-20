from datetime import date

class DateCalculator:
    def years_between_dates(self, date1: date, date2: date) -> int:
        return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = date(2020, 1, 1)
    date_b = date(2023, 4, 15)
    difference = calculator.years_between_dates(date_a, date_b)
    print(difference)