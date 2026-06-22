from datetime import datetime, timedelta

class MonthTimeTracker:
    START_DATE = datetime(2023, 10, 1, 0, 0, 0)
    END_DATE = datetime(2023, 10, 31, 23, 59, 59)

    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end
        self._validate()

    def _validate(self):
        if not isinstance(self.start, datetime) or not isinstance(self.end, datetime):
            raise ValueError("Dates must be datetime objects")
        if self.start > self.end:
            raise ValueError("Start date must precede end date")
        if self.start.year != self.end.year or self.start.month != self.end.month:
            raise ValueError("Start and end dates must be in the same month")

    def get_remaining(self) -> dict:
        delta = self.end - self.start
        total_seconds = int(delta.total_seconds())
        days = total_seconds // 86400
        remainder = total_seconds % 86400
        hours = remainder // 3600
        remainder %= 3600
        minutes = remainder // 60
        seconds = remainder % 60
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": total_seconds
        }

if __name__ == '__main__':
    tracker = MonthTimeTracker(
        datetime(2023, 10, 15, 10, 30, 15),
        datetime(2023, 10, 20, 14, 45, 30)
    )
    result = tracker.get_remaining()
    print(result)