from datetime import date, timedelta
import calendar

class WeekendFinder:
    WEEKDAY_WEEKEND = {5, 6}
    DAYS_IN_WEEK = 7

    @staticmethod
    def _get_days_until_weekend(current_date):
        current_weekday = current_date.weekday()
        if current_weekday in WeekendFinder.WEEKDAY_WEEKEND:
            return 0
        days_ahead = WeekendFinder.DAYS_IN_WEEK - current_weekday
        return days_ahead

    def find_next_weekend_date(self, start_date=None):
        if start_date is None:
            start_date = date.today()
        days_to_add = self._get_days_until_weekend(start_date)
        next_weekend = start_date + timedelta(days=days_to_add)
        return next_weekend

if __name__ == '__main__':
    finder = WeekendFinder()
    sample_date = date(2023, 10, 25)
    result = finder.find_next_weekend_date(sample_date)
    print(result)