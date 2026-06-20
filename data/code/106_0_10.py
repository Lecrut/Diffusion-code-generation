from datetime import date

class DateDifferenceCalculator:
    def __init__(self):
        self.start_date: date = None
        self.end_date: date = None

    def set_dates(self, start_date: date, end_date: date) -> None:
        if not isinstance(start_date, date) or not isinstance(end_date, date):
            raise ValueError("Inputs must be instances of datetime.date.")
        self.start_date = start_date
        self.end_date = end_date

    def calculate_years_difference(self) -> int:
        if self.start_date is None or self.end_date is None:
            raise ValueError("Dates must be set before calculating the difference.")
        return abs((self.end_date - self.start_date).days) // 365

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    sample_start_date = date(1990, 5, 15)
    sample_end_date = date(2023, 4, 10)
    calculator.set_dates(sample_start_date, sample_end_date)
    difference = calculator.calculate_years_difference()
    print(difference)