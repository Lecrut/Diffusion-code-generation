import datetime
class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self._validate_date()
    def _validate_date(self):
        try:
            datetime.date(self.year, self.month, self.day)
        except ValueError:
            raise ValueError("Invalid date provided.")
    def calculate_day_of_year(self):
        day_of_year = datetime.date(self.year, self.month, self.day).timetuple().tm_yday
        return day_of_year
if __name__ == '__main__':
    try:
        calculator1 = DateCalculator(2023, 10, 27)
        print(f"Day of the year for 2023-10-27: {calculator1.calculate_day_of_year()}")
        calculator2 = DateCalculator(2024, 1, 1)
        print(f"Day of the year for 2024-01-01: {calculator2.calculate_day_of_year()}")
        calculator3 = DateCalculator(2023, 2, 30)
        print(f"Attempting invalid date: {calculator3.calculate_day_of_year()}")
    except ValueError as e:
        print(f"Error caught: {e}")