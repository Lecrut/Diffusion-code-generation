from datetime import datetime, timezone

class DateTimeNormalizer:

    def normalize_to_utc(self, time1, time2):
        if time1.tzinfo is None or time1.tzinfo.utcoffset(time1) is None:
            time1 = time1.replace(tzinfo=timezone.utc)
        else:
            time1 = time1.astimezone(timezone.utc)
        if time2.tzinfo is None or time2.tzinfo.utcoffset(time2) is None:
            time2 = time2.replace(tzinfo=timezone.utc)
        else:
            time2 = time2.astimezone(timezone.utc)
        return (time1, time2)
if __name__ == '__main__':
    time1 = datetime(2023, 10, 5, 14, 30)
    time2 = datetime(2023, 10, 5, 9, 45, tzinfo=timezone(timedelta(hours=-7)))
    normalizer = DateTimeNormalizer()
    utc_time1, utc_time2 = normalizer.normalize_to_utc(time1, time2)
    print('UTC Time 1:', utc_time1)
    print('UTC Time 2:', utc_time2)