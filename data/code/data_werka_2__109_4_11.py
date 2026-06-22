import datetime
import calendar

class MonthEndCalculator:
    def __init__(self, reference_date: datetime.datetime):
        if reference_date.tzinfo is not None:
            raise ValueError("Timezone-aware dates are not supported.")
        self.reference_date = reference_date

    def get_days_in_current_month(self) -> int:
        year = self.reference_date.year
        month = self.reference_date.month
        return calendar.monthrange(year, month)[1]

    def get_last_day_of_month(self) -> int:
        return self.get_days_in_current_month()

    def calculate_remaining_hours(self) -> float:
        target_date = self.reference_date
        year = target_date.year
        month = target_date.month
        day = target_date.day
        hour = target_date.hour
        minute = target_date.minute
        second = target_date.second
        microsecond = target_date.microsecond

        days_in_month = self.get_days_in_current_month()
        
        if day == days_in_month:
            if hour == 23 and minute == 59 and second == 59 and microsecond == 999999:
                return 0.0
        
        end_of_month_date = datetime.datetime(year, month, days_in_month)
        end_of_month_date = end_of_month_date.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        time_delta = end_of_month_date - target_date
        total_seconds = time_delta.total_seconds()
        
        if total_seconds < 0:
            return 0.0
            
        return total_seconds / 3600.0

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    calculator = MonthEndCalculator(sample_date)
    days_remaining = calculator.get_last_day_of_month()
    hours_remaining = calculator.calculate_remaining_hours()
    print(f"Days in month: {days_remaining}")
    print(f"Remaining hours: {hours_remaining}")