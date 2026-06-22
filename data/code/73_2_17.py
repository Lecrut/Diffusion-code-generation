from datetime import datetime, timedelta

class TimeCalculator:
    MINUTE_SECONDS = 60
    HOUR_SECONDS = 3600
    DAY_SECONDS = 86400

    def compute_delta_components(self, start: datetime, end: datetime) -> dict:
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("Inputs must be datetime objects")
        if start == end:
            return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}
        delta = end - start
        total_seconds = int(delta.total_seconds())
        sign = 1 if total_seconds >= 0 else -1
        abs_seconds = abs(total_seconds)
        days = abs_seconds // self.DAY_SECONDS
        remaining = abs_seconds % self.DAY_SECONDS
        hours = remaining // self.HOUR_SECONDS
        remaining %= self.HOUR_SECONDS
        minutes = remaining // self.MINUTE_SECONDS
        seconds = remaining % self.MINUTE_SECONDS
        return {
            "days": days * sign,
            "hours": hours * sign,
            "minutes": minutes * sign,
            "seconds": seconds * sign
        }

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = datetime(2023, 6, 15, 8, 30, 0)
    t2 = datetime(2023, 6, 18, 10, 45, 30)
    result = calculator.compute_delta_components(t1, t2)
    print(result)