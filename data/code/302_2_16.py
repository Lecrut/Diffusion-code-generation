class DateCalculator:
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_day_of_month(self, year, month):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        
        days = self.DAYS_IN_MONTH[month]
        if month == 2 and self.is_leap_year(year):
            return days + 1
        return days

if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = calculator.get_day_of_month(year1, month1)
    print(f"Day of the month for {year1}-{month1:02d}: {day1}")