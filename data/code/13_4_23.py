from datetime import datetime, timezone

class DateTimeNormalizer:

    def __init__(self, time1, time2):
        self.time1 = self._normalize_to_utc(time1)
        self.time2 = self._normalize_to_utc(time2)

    def _normalize_to_utc(self, dt):
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    def get_normalized_times(self):
        return (self.time1, self.time2)
if __name__ == '__main__':
    time1 = datetime(2023, 10, 1, 12, 0, tzinfo=timezone(timedelta(hours=-5)))
    time2 = datetime(2023, 10, 1, 18, 0)
    normalizer = DateTimeNormalizer(time1, time2)
    normalized_times = normalizer.get_normalized_times()
    print(normalized_times)