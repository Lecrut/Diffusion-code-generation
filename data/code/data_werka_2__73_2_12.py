from datetime import datetime, timedelta

class TimeCalculator:
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def calculate_difference(self, start: datetime, end: datetime) -> dict:
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("Arguments must be datetime objects")
        delta = end - start
        total_seconds = int(delta.total_seconds())
        abs_seconds = abs(total_seconds)
        sign = 1 if total_seconds >= 0 else -1
        days = abs_seconds // self.SECONDS_PER_DAY
        remainder = abs_seconds % self.SECONDS_PER_DAY
        hours = remainder // self.SECONDS_PER_HOUR
        remainder %= self.SECONDS_PER_HOUR
        minutes = remainder // self.SECONDS_PER_MINUTE
        seconds = remainder % self.SECONDS_PER_MINUTE
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": total_seconds,
            "sign": sign
        }

if __name__ == '__main__':
    calculator = TimeCalculator()
    start_dt = datetime(2024, 6, 1, 8, 0, 0)
    end_dt = datetime(2024, 6, 5, 12, 30, 45)
    result = calculator.calculate_difference(start_dt, end_dt)
    print(result)