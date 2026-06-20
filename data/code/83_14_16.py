from datetime import datetime

class DateTimeComparator:
    def compare(self, dt1: datetime, dt2: datetime) -> bool:
        return dt1 == dt2

if __name__ == '__main__':
    comparator = DateTimeComparator()
    sample_dt1 = datetime(2023, 10, 5, 14, 30)
    sample_dt2 = datetime(2023, 10, 5, 14, 30)
    result = comparator.compare(sample_dt1, sample_dt2)
    print(result)