class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self._validate_date()

    def _validate_date(self):
        if not (1 <= self.month <= 12) or not (1 <= self.day <= [31, 29 if self.is_leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][self.month]):
            raise ValueError("Invalid date provided.")

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def calculate_day_of_year(self):
        day_count = sum([31, 29 if self.is_leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:self.month - 1]) + self.day
        return day_count

if __name__ == '__main__':
    calculator1 = DateCalculator(2023, 4, 15)
    print(calculator1.calculate_day_of_year())