class DateCalculator:
    def get_day_of_month(self, year, month):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        import calendar
        try:
            day = calendar.monthrange(year, month)[1]
            return day
        except ValueError:
            raise ValueError("Invalid year or month combination")
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = calculator.get_day_of_month(year1, month1)
    print(f"Day of the month for {year1}-{month1:02d}: {day1}")
    year2 = 2024
    month2 = 1
    day2 = calculator.get_day_of_month(year2, month2)
    print(f"Day of the month for {year2}-{month2:02d}: {day2}")
    year3 = 2025
    month3 = 12
    day3 = calculator.get_day_of_month(year3, month3)
    print(f"Day of the month for {year3}-{month3:02d}: {day3}")