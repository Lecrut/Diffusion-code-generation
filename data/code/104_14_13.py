import datetime

class DateComparator:
    def __init__(self, date1: str, date2: str):
        self.date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        self.date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')

    def __eq__(self):
        return self.date1 == self.date2

    def is_greater_than(self):
        return self.date1 > self.date2

    def is_less_than(self):
        return self.date1 < self.date2

if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    comparator = DateComparator(date_a, date_b)
    print(f"Date 1 equals Date 2: {comparator.__eq__()}")
    print(f"Date 1 is greater than Date 2: {comparator.is_greater_than()}")
    print(f"Date 1 is less than Date 2: {comparator.is_less_than()}")