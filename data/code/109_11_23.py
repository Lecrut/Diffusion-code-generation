import datetime
import calendar

class MonthTimer:
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    @staticmethod
    def _get_end_of_month(year, month):
        last_day = calendar.monthrange(year, month)[1]
        return datetime.datetime(year, month, last_day, 23, 59, 59)

    @staticmethod
    def calculate_remaining(year, month):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        
        now = datetime.datetime.now()
        target_end = MonthTimer._get_end_of_month(year, month)
        
        if now > target_end:
            return {"hours": 0, "minutes": 0, "seconds": 0}
        
        delta = target_end - now
        total_seconds = int(delta.total_seconds())
        
        hours = total_seconds // MonthTimer.SECONDS_IN_HOUR
        remaining_seconds = total_seconds % MonthTimer.SECONDS_IN_HOUR
        minutes = remaining_seconds // MonthTimer.SECONDS_IN_MINUTE
        seconds = remaining_seconds % MonthTimer.SECONDS_IN_MINUTE
        
        return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = MonthTimer.calculate_remaining(2024, 12)
    print(result)