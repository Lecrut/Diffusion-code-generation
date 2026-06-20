import datetime

class MonthFractionCalculator:
    SECONDS_IN_DAY = 24 * 60 * 60

    @staticmethod
    def _days_in_month(year, month):
        if month == 12:
            next_month_start = datetime.date(year + 1, 1, 1)
        else:
            next_month_start = datetime.date(year, month + 1, 1)
        return (next_month_start - datetime.date(year, month, 1)).days

    @classmethod
    def calculate_remaining_fraction(cls):
        current_date = datetime.datetime.now()
        target_month = 2
        remaining_days = cls._days_in_month(current_date.year, current_date.month) - (current_date.day - 1)
        days_in_target_month = cls._days_in_month(current_date.year if current_date.month < target_month else current_date.year + 1, target_month)
        return remaining_days / days_in_target_month
if __name__ == '__main__':
    calculator = MonthFractionCalculator()
    print(calculator.calculate_remaining_fraction())