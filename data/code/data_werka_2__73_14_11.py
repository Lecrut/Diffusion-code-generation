from datetime import datetime

class TimeDifferenceCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def calculate(start: datetime, end: datetime) -> dict:
        delta = end - start
        total_seconds = int(delta.total_seconds())
        is_negative = total_seconds < 0
        abs_seconds = abs(total_seconds)
        
        hours = abs_seconds // TimeDifferenceCalculator.SECONDS_PER_HOUR
        remainder = abs_seconds % TimeDifferenceCalculator.SECONDS_PER_HOUR
        minutes = remainder // TimeDifferenceCalculator.SECONDS_PER_MINUTE
        seconds = remainder % TimeDifferenceCalculator.SECONDS_PER_MINUTE
        
        multiplier = -1 if is_negative else 1
        return {
            "hours": hours * multiplier,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    start_time = datetime(2023, 1, 1, 10, 0, 0)
    end_time = datetime(2023, 1, 1, 12, 30, 45)
    result = TimeDifferenceCalculator.calculate(start_time, end_time)
    print(result)