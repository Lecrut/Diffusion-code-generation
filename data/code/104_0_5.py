from datetime import datetime

class DateComparator:
    def __init__(self, date1: datetime, date2: datetime):
        self.date1 = date1
        self.date2 = date2
    
    def is_earlier(self) -> bool:
        return self.date1 < self.date2

if __name__ == '__main__':
    sample_date1 = datetime(2023, 10, 1)
    sample_date2 = datetime(2023, 10, 15)
    
    comparator = DateComparator(sample_date1, sample_date2)
    print(comparator.is_earlier())