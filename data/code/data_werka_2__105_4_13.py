from datetime import date, timedelta
import calendar

SATURDAY = 5
SUNDAY = 6

class DateCalculator:
    WEEK_OFFSET = 7

    @staticmethod
    def _days_until(target_weekday, current_weekday):
        diff = target_weekday - current_weekday
        if diff <= 0:
            return DateCalculator.WEEK_OFFSET + diff
        return diff

    def next_saturday(self, current_date):
        current_weekday = current_date.weekday()
        days_to_add = self._days_until(SATURDAY, current_weekday)
        return current_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    start_date = date(2023, 11, 1)
    calculator = DateCalculator()
    result = calculator.next_saturday(start_date)
    print(result)