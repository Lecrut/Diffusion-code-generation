import datetime

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return DAYS_IN_MONTH[month - 1]

class DateCalculator:
    def calculate_time_remaining(self, year, month, day):
        today = datetime.date.today()
        if year < today.year or (year == today.year and month < today.month):
            raise ValueError("Date is in the past")
        if month > today.month or (month == today.month and day > today.day):
            next_month_start = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
            return next_month_start - today
        remaining_days = days_in_month(year, month) - day + 1
        return datetime.timedelta(days=remaining_days)

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    time_left = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(time_left)