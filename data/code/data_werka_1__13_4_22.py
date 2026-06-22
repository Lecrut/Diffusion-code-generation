from datetime import datetime, timezone

class DateTimeNormalizer:

    def normalize_to_utc(self, dt1, dt2):
        if dt1.tzinfo is None:
            dt1 = dt1.replace(tzinfo=timezone.utc)
        else:
            dt1 = dt1.astimezone(timezone.utc)
        if dt2.tzinfo is None:
            dt2 = dt2.replace(tzinfo=timezone.utc)
        else:
            dt2 = dt2.astimezone(timezone.utc)
        return (dt1, dt2)
if __name__ == '__main__':
    naive_dt1 = datetime(2023, 10, 5, 14, 30)
    aware_dt2 = datetime(2023, 10, 6, 9, 15, tzinfo=timezone(timedelta(hours=-7)))
    normalizer = DateTimeNormalizer()
    utc_dt1, utc_dt2 = normalizer.normalize_to_utc(naive_dt1, aware_dt2)
    print('Normalized UTC Time 1:', utc_dt1)
    print('Normalized UTC Time 2:', utc_dt2)