from datetime import datetime

class DateTimeComparator:
    @staticmethod
    def compare(dt1, dt2):
        return dt1 == dt2

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 5, 14, 30)
    sample_dt2 = datetime(2023, 10, 5, 14, 30)
    result = DateTimeComparator.compare(sample_dt1, sample_dt2)
    print(result)