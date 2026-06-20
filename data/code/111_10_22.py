from datetime import datetime

class DateDifferenceCalculator:
    def __init__(self):
        self.date1 = datetime(2023, 9, 1)
        self.date2 = datetime(2023, 10, 15)

    def calculate_difference(self):
        return (self.date2 - self.date1).days

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(f"Days between {calculator.date1.strftime('%Y-%m-%d')} and {calculator.date2.strftime('%Y-%m-%d')}: {calculator.calculate_difference()}")