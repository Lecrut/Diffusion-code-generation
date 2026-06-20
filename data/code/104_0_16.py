from datetime import datetime

class DateComparator:
    @staticmethod
    def is_earlier(date1: datetime, date2: datetime) -> bool:
        return date1 < date2

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 2)
    result = DateComparator.is_earlier(sample_date1, sample_date2)
    print(result)