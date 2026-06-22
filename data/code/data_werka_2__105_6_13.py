from datetime import date, timedelta

class DateCalculator:
    START_DATE = date(2024, 1, 1)
    WEEK_DAYS = 7

    @staticmethod
    def calculate_next_weekly_marker(start_date):
        if not isinstance(start_date, date):
            raise ValueError("start_date must be a date object")
        delta = timedelta(days=DateCalculator.WEEK_DAYS)
        return start_date + delta

if __name__ == '__main__':
    result = DateCalculator.calculate_next_weekly_marker(DateCalculator.START_DATE)
    print(result)