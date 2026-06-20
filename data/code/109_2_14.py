import datetime

class DateCalculator:
    def __init__(self):
        self.months = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def calculate_time_remaining(self, year, month, day):
        today = datetime.date.today()
        if year < today.year or (year == today.year and month < today.month):
            return datetime.timedelta(days=0)
        
        days_in_month = self.months[month]
        if month == 2 and self.is_leap_year(year):
            days_in_month += 1
        
        days_remaining = days_in_month - day
        next_month_start = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
        time_remaining = (next_month_start - today).days + days_remaining
        return datetime.timedelta(days=time_remaining)

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    time_left = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(time_left)