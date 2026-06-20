import datetime

class MonthDaysCalculator:
    def __init__(self):
        self.months = {
            1: 31, 2: 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_last_day_of_month(self, year, month):
        if month == 2:
            return 29 if self.is_leap_year(year) else 28
        return self.months[month]

    def calculate_remaining_days(self, year, month):
        current_date = datetime.date(year, month, 1)
        last_day_of_month = self.get_last_day_of_month(year, month)
        days_difference = (datetime.date(year, month, last_day_of_month) - current_date).days + 1
        return days_difference

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    sample_year = 2023
    sample_month = 4
    remaining_days = calculator.calculate_remaining_days(sample_year, sample_month)
    print(remaining_days)