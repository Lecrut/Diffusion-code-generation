from datetime import date

class DateComparator:
    def __init__(self, date1: date, date2: date):
        self.date1 = date1
        self.date2 = date2

    def compare(self) -> str:
        if self.date1 < self.date2:
            return "date1 is earlier than date2"
        elif self.date1 > self.date2:
            return "date1 is later than date2"
        else:
            return "date1 and date2 are the same"

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 5)
    sample_date2 = date(2023, 10, 10)
    comparator = DateComparator(sample_date1, sample_date2)
    result = comparator.compare()
    print(result)