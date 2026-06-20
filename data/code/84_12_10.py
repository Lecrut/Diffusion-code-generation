import datetime

class DateCalculator:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def get_days_in_month(year, month):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if DateCalculator.is_leap_year(year):
            days_in_month[2] = 29
        return days_in_month

    def get_day_of_year(self, year, month, day):
        days_in_month = self.get_days_in_month(year, month)
        day_of_year = sum(days_in_month[:month]) + day
        return day_of_year

if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = 27
    result1 = calculator.get_day_of_year(year1, month1, day1)
    print(f"Day of the year for {year1}-{month1:02d}-{day1:02d} is: {result1}")