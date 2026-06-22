from datetime import datetime

class DateComparator:
    def __init__(self, first_date: datetime, second_date: datetime):
        if not isinstance(first_date, datetime):
            raise ValueError("first_date must be a datetime object")
        if not isinstance(second_date, datetime):
            raise ValueError("second_date must be a datetime object")
        self.first_date = first_date
        self.second_date = second_date

    def is_first_earlier(self) -> bool:
        return self.first_date < self.second_date

if __name__ == '__main__':
    dt_a = datetime(2024, 12, 25, 0, 0, 0)
    dt_b = datetime(2024, 12, 26, 0, 0, 0)
    comparator = DateComparator(dt_a, dt_b)
    print(comparator.is_first_earlier())