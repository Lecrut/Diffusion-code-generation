from datetime import date

class DateDifference:
    def __init__(self, date1: date, date2: date):
        self.date1 = date1
        self.date2 = date2

    def calculate_difference(self) -> int:
        delta = abs(self.date2 - self.date1)
        return delta.days

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2023, 12, 31)
    difference_calculator = DateDifference(sample_date1, sample_date2)
    print(difference_calculator.calculate_difference())