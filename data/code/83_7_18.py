from datetime import date

class DateComparator:
    def __init__(self, date1: date, date2: date):
        self.date1 = date1
        self.date2 = date2
    
    def is_equal(self) -> bool:
        return self.date1 == self.date2
    
    def compare(self) -> int:
        if self.date1 < self.date2:
            return -1
        elif self.date1 > self.date2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 5)
    sample_date2 = date(2023, 10, 10)
    
    comparator = DateComparator(sample_date1, sample_date2)
    print("Are dates equal?", comparator.is_equal())
    print("Comparison result:", comparator.compare())