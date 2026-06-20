import argparse
from datetime import datetime

class DateComparator:
    def __init__(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
    
    def is_strictly_before(self):
        return self.date1 < self.date2
    
    def compare_dates(self):
        return (self.is_strictly_before(), not self.is_strictly_before())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates.')
    parser.add_argument('date1', type=str, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='Second date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    
    date_a = datetime.strptime(args.date1, '%Y-%m-%d')
    date_b = datetime.strptime(args.date2, '%Y-%m-%d')
    
    comparator = DateComparator(date_a, date_b)
    result_before, result_after = comparator.compare_dates()
    
    print(f"Is {date_a} strictly before {date_b}? {result_before}")
    print(f"Is {date_b} strictly after {date_a}? {result_after}")