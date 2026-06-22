from datetime import datetime, timezone

class DateTimeNormalizer:

    def __init__(self, time1, time2):
        self.time1 = self._to_utc(time1)
        self.time2 = self._to_utc(time2)

    def _to_utc(self, dt):
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    def get_normalized_times(self):
        return (self.time1, self.time2)
if __name__ == '__main__':
    naive_time_str = '2023-10-05T14:48:00'
    aware_time_str = '2023-10-05T09:30:00-05:00'
    time1 = datetime.fromisoformat(naive_time_str)
    time2 = datetime.fromisoformat(aware_time_str)
    normalizer = DateTimeNormalizer(time1, time2)
    utc_times = normalizer.get_normalized_times()
    print('Normalized UTC Time 1:', utc_times[0])
    print('Normalized UTC Time 2:', utc_times[1])