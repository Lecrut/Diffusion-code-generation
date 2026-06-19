from datetime import datetime, timezone

class DateTimeNormalizer:
    def __init__(self, time1_str, time2_str):
        self.time1 = self._parse_time(time1_str)
        self.time2 = self._parse_time(time2_str)

    def _parse_time(self, time_str):
        naive_dt = datetime.fromisoformat(time_str)
        if naive_dt.tzinfo is None:
            return naive_dt.replace(tzinfo=timezone.utc)
        return naive_dt.astimezone(timezone.utc)

    def normalize_times(self):
        return self.time1, self.time2

if __name__ == '__main__':
    time1 = "2023-10-01T15:30:00+02:00"
    time2 = "2023-10-01T09:45:00Z"
    
    normalizer = DateTimeNormalizer(time1, time2)
    normalized_times = normalizer.normalize_times()
    print(normalized_times)