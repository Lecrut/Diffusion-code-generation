import datetime

class DateCalculator:
    def calculate_time_remaining(self, year, month, day):
        today = datetime.date.today()
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError("Invalid date")
        
        next_month_start = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
        time_remaining = (next_month_start - today).days
        return time_remaining

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    try:
        time_left = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
        print(time_left)
    except ValueError as e:
        print(e)