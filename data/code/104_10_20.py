from datetime import date

class DateComparator:
    def __init__(self, first_date: date, second_date: date) -> None:
        self.first_date = first_date
        self.second_date = second_date

    def compare(self) -> int:
        if not isinstance(self.first_date, date):
            raise ValueError("First argument must be a date")
        if not isinstance(self.second_date, date):
            raise ValueError("Second argument must be a date")
        if self.first_date > self.second_date:
            return 1
        if self.first_date < self.second_date:
            return -1
        return 0

if __name__ == '__main__':
    d1 = date(2023, 10, 1)
    d2 = date(2023, 10, 2)
    comparator = DateComparator(d1, d2)
    result = comparator.compare()
    print(result)