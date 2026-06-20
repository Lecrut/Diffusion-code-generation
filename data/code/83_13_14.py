from datetime import date

class DateComparator:

    def __init__(self, date1: date, date2: date):
        if not isinstance(date1, date) or not isinstance(date2, date):
            raise TypeError('Both arguments must be instances of the date class')
        self.date1 = date1
        self.date2 = date2

    def are_dates_same(self) -> bool:
        return self.date1 == self.date2
if __name__ == '__main__':
    comparator1 = DateComparator(date(2023, 4, 1), date(2023, 4, 1))
    print(comparator1.are_dates_same())
    comparator2 = DateComparator(date(2023, 4, 1), date(2023, 4, 2))
    print(comparator2.are_dates_same())