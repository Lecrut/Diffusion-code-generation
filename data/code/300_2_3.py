class DateCalculator:
    def calculate_remaining_days(self, year, month, day):
        import calendar
        import datetime
        current_date = datetime.date(year, month, day)
        if current_date.month == 12:
            next_month = datetime.date(year + 1, 1, 1)
        else:
            next_month = datetime.date(year, month + 1, 1)
        remaining_days = (next_month - current_date).days
        return remaining_days
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = 25
    result1 = calculator.calculate_remaining_days(year1, month1, day1)
    print(f"Remaining days from {year1}-{month1:02d}-{day1:02d}: {result1}")
    year2 = 2024
    month2 = 1
    day2 = 15
    result2 = calculator.calculate_remaining_days(year2, month2, day2)
    print(f"Remaining days from {year2}-{month2:02d}-{day2:02d}: {result2}")
    year3 = 2023
    month3 = 12
    day3 = 31
    result3 = calculator.calculate_remaining_days(year3, month3, day3)
    print(f"Remaining days from {year3}-{month3:02d}-{day3:02d}: {result3}")