class DateCalculator:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self._validate_date()

    def _validate_date(self):
        if not (1 <= self.month <= 12 and 1 <= self.day <= 31):
            raise ValueError('Invalid date provided.')

    def calculate_day_of_year(self):
        leap_years = (self.year - 1) // 4 - (self.year - 1) // 100 + (self.year - 1) // 400
        days_in_month = [31, 28 if not (self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)) else 29] + [31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return leap_years + sum(days_in_month[:self.month - 1]) + self.day
if __name__ == '__main__':
    try:
        calculator1 = DateCalculator(2023, 4, 15)
        print(calculator1.calculate_day_of_year())
        calculator2 = DateCalculator(2020, 2, 29)
        print(calculator2.calculate_day_of_year())
    except ValueError as e:
        print(e)