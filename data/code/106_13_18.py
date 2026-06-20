from datetime import datetime

class DateDifferenceCalculator:
    def __init__(self, timestamp1, timestamp2):
        self.date1 = datetime.fromtimestamp(timestamp1)
        self.date2 = datetime.fromtimestamp(timestamp2)

    def calculate_year_difference(self):
        return abs(self.date1.year - self.date2.year)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator(1609459200, 1672531200)
    print(calculator.calculate_year_difference())