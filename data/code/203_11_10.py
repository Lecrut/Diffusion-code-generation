from datetime import datetime, timedelta

class DateTimeComparer:
    EPOCH = datetime(1970, 1, 1)

    @staticmethod
    def to_utc(dt):
        if dt.tzinfo is not None:
            return dt.astimezone(datetime.utc)
        return dt.replace(tzinfo=None)

    @classmethod
    def difference_in_seconds(cls, dt1, dt2):
        utc_dt1 = cls.to_utc(dt1)
        utc_dt2 = cls.to_utc(dt2)
        return abs((utc_dt1 - utc_dt2).total_seconds())

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    dt2 = datetime(2023, 10, 1, 12, 0, 5, tzinfo=datetime.timezone.utc)
    result = DateTimeComparer.difference_in_seconds(dt1, dt2)
    print(result)