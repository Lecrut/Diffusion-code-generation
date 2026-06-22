from datetime import datetime, time, timedelta
from typing import Optional

class ElapsedTimeCalculator:
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    def __init__(self, reference: datetime):
        if not isinstance(reference, datetime):
            raise ValueError("Reference must be a datetime instance")
        if reference.tzinfo is not None:
            raise ValueError("Reference must be naive")
        self.reference = reference

    def compute_since_midnight(self) -> str:
        midnight = datetime.combine(self.reference.date(), time.min)
        delta = self.reference - midnight
        total_seconds = int(delta.total_seconds())
        if not (0 <= total_seconds < self.SECONDS_IN_DAY):
            raise ValueError("Time must be within the current day")
        hours = total_seconds // self.SECONDS_IN_HOUR
        remainder = total_seconds % self.SECONDS_IN_HOUR
        minutes = remainder // 60
        seconds = remainder % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 27, 14, 30, 45)
    calculator = ElapsedTimeCalculator(sample_datetime)
    output = calculator.compute_since_midnight()
    print(output)