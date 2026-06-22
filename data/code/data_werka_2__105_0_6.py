from datetime import datetime, timedelta

class DateCalculator:
    MONDAY = 0
    WEEK_DAYS = 7

    @staticmethod
    def get_next_weekday(current_date, target_weekday):
        current_weekday = current_date.weekday()
        days_ahead = (target_weekday - current_weekday) % DateCalculator.WEEK_DAYS
        if days_ahead == 0:
            days_ahead = DateCalculator.WEEK_DAYS
        return current_date + timedelta(days=days_ahead)

    @staticmethod
    def get_next_monday(reference_date=None):
        if reference_date is None:
            reference_date = datetime.today()
        return DateCalculator.get_next_weekday(reference_date, DateCalculator.MONDAY)

if __name__ == '__main__':
    calculator = DateCalculator()
    today = datetime.today()
    next_monday = calculator.get_next_monday(today)
    print(next_monday.strftime('%Y-%m-%d'))