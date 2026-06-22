import datetime

class MonthCalculator:
    DAYS_IN_WEEK = 7
    MONTHS_IN_YEAR = 12

    @staticmethod
    def get_next_month_first(year, month):
        if month == 12:
            return datetime.date(year + 1, 1, 1)
        return datetime.date(year, month + 1, 1)

    @staticmethod
    def get_last_day_of_month(year, month):
        next_month = MonthCalculator.get_next_month_first(year, month)
        return next_month - datetime.timedelta(days=1)

    def calculate_remaining_days(self, year, month, day):
        last_day = self.get_last_day_of_month(year, month)
        if day > last_day.day:
            raise ValueError("Day exceeds month limits")
        current = datetime.date(year, month, day)
        remaining = (last_day - current).days
        return remaining

if __name__ == '__main__':
    calculator = MonthCalculator()
    result = calculator.calculate_remaining_days(2024, 2, 10)
    print(result)