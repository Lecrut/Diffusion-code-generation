import datetime

class RemainingMinutesCalculator:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def calculate_remaining_minutes(self):
        current_date = datetime.date(self.year, self.month, 1)
        if self.month == 12:
            next_month = 1
            next_year = self.year + 1
        else:
            next_month = self.month + 1
            next_year = self.year

        last_day_of_next_month = (datetime.date(next_year, next_month, 1) + datetime.timedelta(days=31)).replace(day=1) - datetime.timedelta(days=1)
        if next_month == 12:
            last_day_of_next_month = datetime.date(next_year, 12, 31)
        else:
            last_day_of_next_month = (datetime.date(next_year, next_month + 1, 1) + datetime.timedelta(days=30)).replace(day=1) - datetime.timedelta(days=1)

        days_diff = (last_day_of_next_month - current_date).days
        remaining_minutes = days_diff * 24 * 60
        return remaining_minutes

if __name__ == '__main__':
    calculator = RemainingMinutesCalculator(2023, 10)
    print(calculator.calculate_remaining_minutes())