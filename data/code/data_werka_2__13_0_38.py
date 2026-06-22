from datetime import datetime, timedelta

class TimeDeltaCalculator:
    @staticmethod
    def calculate_time_delta(dt1, dt2):
        if not (dt1.tzinfo and dt2.tzinfo):
            raise ValueError("Both datetimes must be timezone-aware")
        return abs(dt1 - dt2)

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, tzinfo=datetime.timezone.utc)
    dt2 = datetime(2023, 10, 2, 14, 30, tzinfo=datetime.timezone.utc)
    delta = TimeDeltaCalculator.calculate_time_delta(dt1, dt2)
    print(delta)