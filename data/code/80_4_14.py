import argparse
from datetime import datetime

class DateComparator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Compare two dates")
        self.parser.add_argument("date1", type=str, help="First date in YYYY-MM-DD format")
        self.parser.add_argument("date2", type=str, help="Second date in YYYY-MM-DD format")

    def parse_arguments(self):
        args = self.parser.parse_args()
        return datetime.strptime(args.date1, "%Y-%m-%d"), datetime.strptime(args.date2, "%Y-%m-%d")

    def compare_dates(self, date1, date2):
        if date1 < date2:
            print(f"{date1} is strictly before {date2}")
        elif date2 < date1:
            print(f"{date2} is strictly before {date1}")
        else:
            print(f"{date1} and {date2} are the same")

if __name__ == '__main__':
    comparator = DateComparator()
    date_a, date_b = comparator.parse_arguments()
    comparator.compare_dates(date_a, date_b)