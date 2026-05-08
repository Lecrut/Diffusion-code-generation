class DateCalculator:
    def calculate_time_remaining(self, year, month, day):
        import datetime
        today = datetime.date.today()
        if month == today.month and year == today.year:
            days_remaining = (datetime.date(year, month + 1, 1) - today).days
            return days_remaining
        else:
            first_day_of_next_month = datetime.date(year, month + 1, 1)
            days_in_current_month = (first_day_of_next_month - today).days
            return days_in_current_month
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    time_left = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(f"For the month of {sample_month}/{sample_year}, starting from {sample_day}:")
    print(f"Time remaining until the next month starts: {time_left} days")