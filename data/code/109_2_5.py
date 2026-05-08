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
            target_date = datetime.date(year, month, day)
            if target_date.month == datetime.date.today().month and target_date.year == datetime.date.today().year:
                days_left = (datetime.date(target_date.year, target_date.month + 1, 1) - target_date).days
                return days_left
            else:
                if month == 12:
                    next_month = datetime.date(year + 1, 1, 1)
                else:
                    next_month = datetime.date(year, month + 1, 1)
                last_day_of_month = next_month - datetime.timedelta(days=1)
                days_remaining = (last_day_of_month - target_date).days
                return days_remaining
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    print(f"Time remaining in month {sample_month}/{sample_year} starting from day {sample_day}:")
    result1 = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(result1)
    sample_year = 2024
    sample_month = 1
    sample_day = 31
    print(f"\nTime remaining in month {sample_month}/{sample_year} starting from day {sample_day}:")
    result2 = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(result2)
    sample_year = 2023
    sample_month = 4
    sample_day = 1
    print(f"\nTime remaining in month {sample_month}/{sample_year} starting from day {sample_day}:")
    result3 = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(result3)