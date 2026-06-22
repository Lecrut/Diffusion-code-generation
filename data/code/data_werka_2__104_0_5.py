from datetime import datetime

class DateComparator:
    MIN_DATE = datetime.min

    @staticmethod
    def validate_date(dt: datetime) -> None:
        if dt is None:
            raise ValueError("Date cannot be None")
        if dt < DateComparator.MIN_DATE:
            raise ValueError("Date is out of supported range")

    @staticmethod
    def is_earlier(first: datetime, second: datetime) -> bool:
        DateComparator.validate_date(first)
        DateComparator.validate_date(second)
        return first < second

if __name__ == '__main__':
    date_a = datetime(2024, 11, 10, 14, 30, 0)
    date_b = datetime(2024, 11, 11, 14, 30, 0)
    result = DateComparator.is_earlier(date_a, date_b)
    print(result)