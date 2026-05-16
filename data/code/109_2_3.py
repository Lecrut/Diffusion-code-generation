class DateCalculator:
    def calculate_time_remaining(self, year, month, day):
        import datetime
        today = datetime.date.today()
        if month == today.month and year == today.year:
            days_remaining = 31 - day
            if day > 31:
                days_remaining = 0
            elif day <= 31:
                days_remaining = 31 - day
            else:
                days_remaining = 0
            if day == 31:
                days_remaining = 0
            else:
                days_remaining = 31 - day
        else:
            if month == 12:
                days_in_month = 31
            elif month in [4, 6, 9, 11]:
                days_in_month = 30
            else:
                days_in_month = 31
            days_remaining = days_in_month - day
        return days_remaining
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = 15
    result1 = calculator.calculate_time_remaining(year1, month1, day1)
    print(f"Time remaining in {year1}-{month1}: {result1} days")
    year2 = 2023
    month2 = 4
    day2 = 20
    result2 = calculator.calculate_time_remaining(year2, month2, day2)
    print(f"Time remaining in {year2}-{month2}: {result2} days")
    year3 = 2023
    month3 = 12
    day3 = 31
    result3 = calculator.calculate_time_remaining(year3, month3, day3)
    print(f"Time remaining in {year3}-{month3}: {result3} days")
    year4 = 2023
    month4 = 1
    day4 = 30
    result4 = calculator.calculate_time_remaining(year4, month4, day4)
    print(f"Time remaining in {year4}-{month4}: {result4} days")