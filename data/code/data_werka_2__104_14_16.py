import datetime
import time

class DateComparator:
    def __init__(self, first_date, second_date):
        self._first = first_date
        self._second = second_date
        self._first_ts = self._to_timestamp(first_date)
        self._second_ts = self._to_timestamp(second_date)
        self._equal = self._first_ts == self._second_ts
        self._greater = self._first_ts > self._second_ts
        self._less = self._first_ts < self._second_ts

    @staticmethod
    def _to_timestamp(d):
        if isinstance(d, datetime.datetime):
            return d.timestamp()
        if isinstance(d, datetime.date):
            return time.mktime(d.timetuple())
        raise ValueError("Unsupported date type")

    def is_equal(self):
        return self._equal

    def is_greater_than(self):
        return self._greater

    def is_less_than(self):
        return self._less

    def get_first(self):
        return self._first

    def get_second(self):
        return self._second

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 15)
    d2 = datetime.date(2023, 1, 15)
    d3 = datetime.date(2023, 1, 20)
    
    comp1 = DateComparator(d1, d2)
    comp2 = DateComparator(d1, d3)
    comp3 = DateComparator(d3, d1)
    
    print(comp1.is_equal())
    print(comp1.is_greater_than())
    print(comp1.is_less_than())
    print(comp2.is_equal())
    print(comp2.is_greater_than())
    print(comp2.is_less_than())
    print(comp3.is_equal())
    print(comp3.is_greater_than())
    print(comp3.is_less_than())