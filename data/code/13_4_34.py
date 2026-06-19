from datetime import datetime, timezone

class DateTimeNormalizer:

    def normalize_to_utc(self, time1, time2):
        utc_time1 = self._to_utc(time1)
        utc_time2 = self._to_utc(time2)
        return (utc_time1, utc_time2)

    def _to_utc(self, dt):
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        else:
            return dt.astimezone(timezone.utc)
if __name__ == '__main__':
    time1 = datetime(2023, 10, 1, 12, 0, tzinfo=timezone(timedelta(hours=-5)))
    time2 = datetime(2023, 10, 1, 9, 0, tzinfo=timezone(timedelta(hours=2)))
    normalizer = DateTimeNormalizer()
    utc_time1, utc_time2 = normalizer.normalize_to_utc(time1, time2)
    print('Normalized UTC Time 1:', utc_time1)
    print('Normalized UTC Time 2:', utc_time2)