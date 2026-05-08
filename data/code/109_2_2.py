class DateCalculator:
    def calculate_time_remaining(self, year, month, day):
        import datetime
        today = datetime.date.today()
        if month == today.month and year == today.year:
            days_remaining = 31 - day
            if day == 31:
                days_remaining = 0
            return days_remaining
        else:
            current_month_days = 0
            if month == 1:
                current_month_days = 31
            elif month == 2:
                current_month_days = 28 if not (datetime.date.today().year % 4 == 0 and datetime.date.today().year % 100 != 0 or datetime.date.today().year % 400 == 0) else 29
            elif month == 3:
                current_month_days = 31
            elif month == 4:
                current_month_days = 30
            elif month == 5:
                current_month_days = 31
            elif month == 6:
                current_month_days = 30
            elif month == 7:
                current_month_days = 31
            elif month == 8:
                current_month_days = 31
            elif month == 9:
                current_month_days = 30
            elif month == 10:
                current_month_days = 31
            elif month == 11:
                current_month_days = 30
            elif month == 12:
                current_month_days = 31
            target_month_days_passed = 0
            if month == today.month:
                target_month_days_passed = day
            else:
                if month == 2:
                    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                    days_in_month = 29 if is_leap else 28
                elif month in [4, 6, 9, 11]:
                    days_in_month = 30
                else:
                    days_in_month = 31
                days_remaining = days_in_month - day
                return days_remaining
        return 0
if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2024
    month1 = 1
    day1 = 15
    result1 = calculator.calculate_time_remaining(year1, month1, day1)
    print(f"Time remaining in {year1}-{month1}: {result1} days")
    year2 = 2024
    month2 = 4
    day2 = 10
    result2 = calculator.calculate_time_remaining(year2, month2, day2)
    print(f"Time remaining in {year2}-{month2}: {result2} days")
    year3 = 2023
    month3 = 2
    day3 = 10
    result3 = calculator.calculate_time_remaining(year3, month3, day3)
    print(f"Time remaining in {year3}-{month3}: {result3} days")
    year4 = 2024
    month4 = 2
    day4 = 1
    result4 = calculator.calculate_time_remaining(year4, month4, day4)
    print(f"Time remaining in {year4}-{month4}: {result4} days")