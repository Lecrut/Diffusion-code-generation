class DateCalculator:
    def calculate_time_remaining(self, year, month, day):
        import datetime
        today = datetime.date.today()
        if month == today.month and year == today.year:
            days_remaining = 31 - day
            if day == 31:
                days_remaining = 0
            return days_remaining
        if month > today.month:
            next_month = today.replace(year=year, month=month, day=1) + datetime.timedelta(days=31)
            return (next_month - today).days
        if month < today.month:
            prev_month = today.replace(year=year, month=month, day=1) - datetime.timedelta(days=31)
            return (today - prev_month).days
        return 0
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2024
    sample_month = 12
    sample_day = 25
    time_left = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(f"Time remaining in {sample_year}-{sample_month}-{sample_day}: {time_left} days")