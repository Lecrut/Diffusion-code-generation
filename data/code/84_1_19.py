class DateCalculator:
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def calculate_day_of_year(self, year, month, day):
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        if day < 1 or day > self.DAYS_IN_MONTH[month]:
            if month == 2 and day == 29 and not self.is_leap_year(year):
                raise ValueError("Invalid date for non-leap year")
            raise ValueError(f"Day must be between 1 and {self.DAYS_IN_MONTH[month]}")

        cumulative_days = sum(self.DAYS_IN_MONTH[:month]) + day
        if month > 2 and self.is_leap_year(year):
            cumulative_days += 1

        return cumulative_days

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_day_of_year(2023, 10, 26))
    print(calculator.calculate_day_of_year(2024, 1, 1))
    print(calculator.calculate_day_of_year(2000, 2, 29))
    print(calculator.calculate_day_of_year(2023, 12, 31))
    print(calculator.calculate_day_of_year(2023, 1, 1))
    print(calculator.calculate_day_of_year(2023, 3, 1))