from datetime import datetime, timedelta

class DateCalculator:
    FRIDAY_WEEKDAY = 4
    DAYS_IN_WEEK = 7

    @staticmethod
    def get_upcoming_friday(reference_date):
        current_weekday = reference_date.weekday()
        days_ahead = DateCalculator.FRIDAY_WEEKDAY - current_weekday
        if days_ahead <= 0:
            days_ahead += DateCalculator.DAYS_IN_WEEK
        return reference_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    ref_date = datetime(2023, 12, 15)
    calculator = DateCalculator()
    result = calculator.get_upcoming_friday(ref_date)
    print(result.strftime("%Y-%m-%d"))