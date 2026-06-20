from datetime import datetime

class DateDifference:
    def __init__(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
    
    def calculate_difference(self):
        delta = abs((self.date2 - self.date1).days)
        return delta

if __name__ == '__main__':
    date1 = datetime(2023, 9, 1)
    date2 = datetime(2023, 10, 15)
    
    diff_instance = DateDifference(date1, date2)
    print(f"Days between {date1.date()} and {date2.date()}: {diff_instance.calculate_difference()}")