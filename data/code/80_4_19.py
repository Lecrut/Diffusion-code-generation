import argparse
from datetime import datetime

class DateComparator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Compare two dates.")
        self.parser.add_argument("date1", type=datetime.fromisoformat, help="First date in ISO format")
        self.parser.add_argument("date2", type=datetime.fromisoformat, help="Second date in ISO format")

    def compare(self):
        args = self.parser.parse_args()
        return args.date1 < args.date2

if __name__ == '__main__':
    comparator = DateComparator()
    print(f"Is {comparator.parser.parse_args().date1} strictly before {comparator.parser.parse_args().date2}? {comparator.compare()}")