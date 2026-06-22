import datetime
import calendar

class MonthTimer:
    def __init__(self, reference_date: datetime.datetime):
        if reference_date.tzinfo is not None:
            raise ValueError("Timezone-aware dates are not supported.")
        if reference_date.microsecond != 0:
            raise ValueError("Microseconds are not supported for integer hour calculations.")
        self.reference_date = reference_date

    def get_remaining_hours(self) -> float:
        year = self.reference_date.year
        month = self.reference_date.month
        _, days_in_month = calendar.monthrange(year, month)
        last_day_of_month = datetime.datetime(year, month, days_in_month)
        end_of_day = last_day_of_month.replace(hour=23, minute=59, second=59, microsecond=999999)
        delta = end_of_day - self.reference_date
        total_seconds = delta.total_seconds()
        if total_seconds < 0:
            return 0.0
        return total_seconds / 3600

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    timer = MonthTimer(sample_date)
    print(timer.get_remaining_hours())