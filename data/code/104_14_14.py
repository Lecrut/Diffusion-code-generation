from datetime import date

class DateComparator:

    def __init__(self, date1: date, date2: date):
        self._date1 = date1
        self._date2 = date2

    def __eq__(self, other):
        if not isinstance(other, DateComparator):
            return NotImplemented
        return self._date1 == other._date1 and self._date2 == other._date2

    def __gt__(self, other):
        if not isinstance(other, DateComparator):
            return NotImplemented
        return self._date1 > other._date1 or (self._date1 == other._date1 and self._date2 > other._date2)

    def __lt__(self, other):
        if not isinstance(other, DateComparator):
            return NotImplemented
        return self._date1 < other._date1 or (self._date1 == other._date1 and self._date2 < other._date2)
if __name__ == '__main__':
    date_comp = DateComparator(date(2023, 4, 1), date(2023, 4, 2))
    print(date_comp == DateComparator(date(2023, 4, 1), date(2023, 4, 2)))
    print(date_comp > DateComparator(date(2023, 4, 1), date(2023, 4, 2)))
    print(date_comp < DateComparator(date(2023, 4, 1), date(2023, 4, 2)))