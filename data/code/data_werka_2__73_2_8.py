from datetime import datetime, timedelta

class TimeCalculator:
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    @staticmethod
    def _ensure_datetime(value):
        if not isinstance(value, datetime):
            raise ValueError("Argument must be a datetime object")
        return value

    def calculate_difference(self, start_time, end_time):
        t1 = self._ensure_datetime(start_time)
        t2 = self._ensure_datetime(end_time)
        delta = t2 - t1
        total_seconds = delta.total_seconds()
        abs_seconds = abs(total_seconds)
        days = int(abs_seconds // self.SECONDS_IN_DAY)
        remainder = int(abs_seconds % self.SECONDS_IN_DAY)
        hours = remainder // self.SECONDS_IN_HOUR
        remainder %= self.SECONDS_IN_HOUR
        minutes = remainder // self.SECONDS_IN_MINUTE
        seconds = remainder % self.SECONDS_IN_MINUTE
        sign = -1 if total_seconds < 0 else 1
        return timedelta(
            days=days * sign,
            hours=hours * sign,
            minutes=minutes * sign,
            seconds=seconds * sign
        )

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime(2024, 5, 1, 8, 0, 0)
    end = datetime(2024, 5, 1, 12, 30, 45)
    diff = calculator.calculate_difference(start, end)
    print(diff)