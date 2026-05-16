class DateCalculator:
    def calculate_time_remaining(self, year, month, day):
        import datetime
        today = datetime.date.today()
        if month == today.month and year == today.year:
            return 0
        first_day_of_next_month = today.replace(day=1) + datetime.timedelta(days=32)
        if first_day_of_next_month.month == today.month:
            first_day_of_next_month = first_day_of_next_month + datetime.timedelta(days=32)
        next_month_start = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
        time_remaining = (next_month_start - today).days
        return time_remaining
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    time_left = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(f"Time remaining until the start of the next month from {sample_year}-{sample_month}-{sample_day}: {time_left} days")