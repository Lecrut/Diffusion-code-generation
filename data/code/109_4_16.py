import datetime
import calendar

class MonthDurationCalculator:
    HOURS_PER_DAY = 24.0
    SECONDS_PER_HOUR = 3600.0

    @staticmethod
    def get_last_day_of_month(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def calculate_remaining_hours(target_date: datetime.datetime) -> float:
        if target_date.tzinfo is not None:
            raise ValueError("Timezone-aware dates are not supported.")
        
        year = target_date.year
        month = target_date.month
        last_day = MonthDurationCalculator.get_last_day_of_month(year, month)
        
        end_of_month = datetime.datetime(year, month, last_day, 23, 59, 59, 999999)
        
        delta = end_of_month - target_date
        total_seconds = delta.total_seconds()
        
        if total_seconds < 0:
            return 0.0
            
        return total_seconds / MonthDurationCalculator.SECONDS_PER_HOUR

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    result = MonthDurationCalculator.calculate_remaining_hours(sample_date)
    print(result)