from datetime import timedelta
from calendar import monthrange

class MonthRemainderCalculator:
    START_HOUR = 0
    START_MINUTE = 0
    START_SECOND = 0
    END_HOUR = 23
    END_MINUTE = 59
    END_SECOND = 59

    @staticmethod
    def calculate(year: int, month: int, current_day: int, current_hour: int, current_minute: int, current_second: int) -> timedelta:
        days_in_month = monthrange(year, month)[1]
        start_dt = MonthRemainderCalculator._create_time(year, month, 1, MonthRemainderCalculator.START_HOUR, MonthRemainderCalculator.START_MINUTE, MonthRemainderCalculator.START_SECOND)
        end_dt = MonthRemainderCalculator._create_time(year, month, days_in_month, MonthRemainderCalculator.END_HOUR, MonthRemainderCalculator.END_MINUTE, MonthRemainderCalculator.END_SECOND)
        current_dt = MonthRemainderCalculator._create_time(year, month, current_day, current_hour, current_minute, current_second)
        
        if current_dt <= start_dt:
            return end_dt - start_dt
        if current_dt >= end_dt:
            return timedelta(0)
        return end_dt - current_dt

    @staticmethod
    def _create_time(year: int, month: int, day: int, hour: int, minute: int, second: int):
        from datetime import datetime
        return datetime(year, month, day, hour, minute, second)

if __name__ == '__main__':
    result = MonthRemainderCalculator.calculate(2023, 10, 15, 12, 0, 0)
    print(result)