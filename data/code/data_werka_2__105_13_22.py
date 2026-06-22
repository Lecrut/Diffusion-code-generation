from datetime import date, timedelta

class WeekendFinder:
    SATURDAY = 5
    SUNDAY = 6
    WEEKDAY_MASK = 0b00011111

    @staticmethod
    def _days_until_weekend(current_date: date) -> int:
        current_weekday = current_date.weekday()
        if current_weekday <= WeekendFinder.SATURDAY:
            return WeekendFinder.SATURDAY - current_weekday
        return WeekendFinder.SATURDAY + (7 - current_weekday)

    def find_next_saturday(self, reference_date: date = None) -> date:
        if reference_date is None:
            reference_date = date.today()
        days_offset = self._days_until_weekend(reference_date)
        return reference_date + timedelta(days=days_offset)

if __name__ == '__main__':
    finder = WeekendFinder()
    result = finder.find_next_saturday()
    print(result)