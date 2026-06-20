import datetime

class MonthRemainingCalculator:
    @staticmethod
    def calculate_remaining_days(current_date):
        target_date = datetime.date(current_date.year, current_date.month + 1, 1) - datetime.timedelta(days=1)
        time_difference = target_date - current_date
        return time_difference.days

if __name__ == '__main__':
    current_date = datetime.date(2024, 6, 15)
    remaining_days = MonthRemainingCalculator.calculate_remaining_days(current_date)
    print(remaining_days)