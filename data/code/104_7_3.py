from datetime import datetime, timezone, timedelta
import calendar

class DateTimeComparator:
    BASE_SECONDS_HOUR = 3600

    def __init__(self, reference_dt: datetime = None):
        if reference_dt is not None:
            self.set_reference(reference_dt)
        else:
            self.reference = datetime.now(timezone.utc)

    def set_reference(self, dt: datetime):
        self.validate_timezone(dt)
        self.reference = dt.astimezone(timezone.utc)

    def validate_timezone(self, dt: datetime):
        if not hasattr(dt, 'tzinfo') or dt.tzinfo is None:
            raise ValueError("Datetime object must be timezone-aware")

    def calculate_delta_hours(self, target_dt: datetime) -> float:
        self.validate_timezone(target_dt)
        target_utc = target_dt.astimezone(timezone.utc)
        diff = target_utc - self.reference
        return diff.total_seconds() / self.BASE_SECONDS_HOUR

    def compare(self, dt1: datetime, dt2: datetime) -> str:
        self.validate_timezone(dt1)
        self.validate_timezone(dt2)
        d1_utc = dt1.astimezone(timezone.utc)
        d2_utc = dt2.astimezone(timezone.utc)
        if d1_utc > d2_utc:
            return "greater"
        elif d1_utc < d2_utc:
            return "lesser"
        return "equal"

if __name__ == '__main__':
    tz_est = timezone(timedelta(hours=-5))
    tz_pst = timezone(timedelta(hours=-8))
    dt1 = datetime(2023, 11, 1, 12, 0, 0, tzinfo=tz_est)
    dt2 = datetime(2023, 11, 1, 10, 0, 0, tzinfo=tz_pst)
    
    comp = DateTimeComparator(dt1)
    delta = comp.calculate_delta_hours(dt2)
    print(delta)
    
    status = comp.compare(dt1, dt2)
    print(status)