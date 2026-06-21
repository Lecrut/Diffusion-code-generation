from datetime import datetime

class DateTimeComparator:
    MIN_DATE = datetime.min

    @staticmethod
    def validate_date(value):
        if not isinstance(value, datetime):
            raise ValueError("Expected datetime instance")
        return value

    def is_first_earlier(self, first: datetime, second: datetime) -> bool:
        self.validate_date(first)
        self.validate_date(second)
        if first == self.MIN_DATE or second == self.MIN_DATE:
            return first == self.MIN_DATE and second != self.MIN_DATE
        return first < second

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1, 12, 0, 0)
    dt2 = datetime(2023, 1, 2, 12, 0, 0)
    comparator = DateTimeComparator()
    result = comparator.is_first_earlier(dt1, dt2)
    print(result)