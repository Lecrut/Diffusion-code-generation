from datetime import date

class DateComparator:
    def __init__(self, date1: date, date2: date):
        self.date1 = date1
        self.date2 = date2

    def is_before(self) -> bool:
        return self.date1 < self.date2

if __name__ == '__main__':
    comparator = DateComparator(date(2023, 10, 26), date(2023, 10, 20))
    print(comparator.is_before())