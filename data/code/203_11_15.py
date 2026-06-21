from datetime import datetime

class DateTimeComparator:
    @staticmethod
    def difference_in_seconds(dt1: datetime, dt2: datetime) -> int:
        if not dt1.tzinfo or not dt2.tzinfo:
            raise ValueError("Both datetimes must be timezone-aware.")
        return abs((dt1 - dt2).total_seconds())

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    dt2 = datetime(2023, 10, 1, 14, 0, 0, tzinfo=datetime.timezone.utc)
    print(DateTimeComparator.difference_in_seconds(dt1, dt2))