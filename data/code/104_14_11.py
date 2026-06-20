import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, date1, date2):
        self.date1 = datetime.datetime.strptime(date1, self.DATE_FORMAT)
        self.date2 = datetime.datetime.strptime(date2, self.DATE_FORMAT)

    def equals(self):
        return self.date1 == self.date2

    def greater_than(self):
        return self.date1 > self.date2

    def less_than(self):
        return self.date1 < self.date2

if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    comparator = DateComparator(date_a, date_b)
    print("Date 1 equals Date 2:", comparator.equals())
    print("Date 1 is greater than Date 2:", comparator.greater_than())
    print("Date 1 is less than Date 2:", comparator.less_than())

    date_c = "2024-01-01"
    comparator = DateComparator(date_a, date_c)
    print("Date 1 equals Date 3:", comparator.equals())
    print("Date 1 is greater than Date 3:", comparator.greater_than())
    print("Date 1 is less than Date 3:", comparator.less_than())