class DateCalculator:
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_YEAR_THRESHOLD_1 = 4
    LEAP_YEAR_THRESHOLD_2 = 100
    LEAP_YEAR_THRESHOLD_3 = 400

    def is_leap_year(self, year):
        return (year % self.LEAP_YEAR_THRESHOLD_1 == 0 and year % self.LEAP_YEAR_THRESHOLD_2 != 0) or (year % self.LEAP_YEAR_THRESHOLD_3 == 0)

    def calculate_day_of_year(self, year, month, day):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1 <= day <= self.DAYS_IN_MONTH[month]):
            raise ValueError(f"Day must be between 1 and {self.DAYS_IN_MONTH[month]} for the given month")

        if month == 2 and self.is_leap_year(year):
            self.DAYS_IN_MONTH[2] = 29

        day_of_year = sum(self.DAYS_IN_MONTH[:month]) + day
        return day_of_year

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_day_of_year(2023, 10, 26))
    print(calculator.calculate_day_of_year(2024, 1, 1))
    print(calculator.calculate_day_of_year(2000, 2, 29))
    print(calculator.calculate_day_of_year(2023, 12, 31))
    print(calculator.calculate_day_of_year(2023, 1, 1))
    print(calculator.calculate_day_of_year(2023, 3, 1))