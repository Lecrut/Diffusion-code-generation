import argparse
from datetime import date

class DateDifferenceCalculator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Calculate the difference in days between two dates.')
        self.parser.add_argument('date1', type=date.fromisoformat, help='First date in ISO format')
        self.parser.add_argument('date2', type=date.fromisoformat, help='Second date in ISO format')

    def calculate_difference(self):
        args = self.parser.parse_args()
        earlier_date = min(args.date1, args.date2)
        later_date = max(args.date1, args.date2)
        return (later_date - earlier_date).days

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result1 = calculator.calculate_difference()
    print(result1)
    result2 = calculator.calculate_difference()
    print(result2)