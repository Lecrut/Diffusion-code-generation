from datetime import date

class DateComparator:
    def __init__(self, first_date: date, second_date: date):
        self.first_date = first_date
        self.second_date = second_date

    def get_days_difference(self) -> int:
        delta = self.second_date - self.first_date
        return delta.days

    def get_absolute_difference(self) -> int:
        return abs(self.get_days_difference())

if __name__ == '__main__':
    d1 = date(2024, 5, 1)
    d2 = date(2024, 5, 15)
    comparator = DateComparator(d1, d2)
    print(comparator.get_days_difference())
    print(comparator.get_absolute_difference())