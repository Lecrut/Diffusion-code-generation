from datetime import date

class DateDifferenceCalculator:
    def __init__(self, date1: date, date2: date):
        self.date1 = min(date1, date2)
        self.date2 = max(date1, date2)

    def calculate_years(self) -> int:
        return self.date2.year - self.date1.year

    def calculate_months(self) -> int:
        return (self.date2.month - self.date1.month) + 12 * (self.date2.year - self.date1.year - 1)

    def get_difference_in_months_and_years(self) -> tuple:
        years = self.calculate_years()
        months = self.calculate_months()
        return years, months

if __name__ == '__main__':
    sample_date1 = date(2010, 5, 15)
    sample_date2 = date(2023, 8, 20)
    calculator = DateDifferenceCalculator(sample_date1, sample_date2)
    years, months = calculator.get_difference_in_months_and_years()
    print(f"Years: {years}, Months: {months}")