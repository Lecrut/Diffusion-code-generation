from datetime import datetime

class DateTimeComparator:
    @staticmethod
    def compare_datetimes_ignoring_time(dt1: datetime, dt2: datetime) -> bool:
        return dt1.date() == dt2.date()

if __name__ == '__main__':
    comparator = DateTimeComparator()
    dt1 = datetime(2023, 4, 15, 12, 30)
    dt2 = datetime(2023, 4, 15, 18, 45)
    result = comparator.compare_datetimes_ignoring_time(dt1, dt2)
    print(result)