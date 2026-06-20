import argparse
from datetime import date

def days_difference(date1: date, date2: date) -> int:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError('Both arguments must be instances of date')
    return abs((date2 - date1).days)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference in days between two dates.')
    parser.add_argument('date1', type=date.fromisoformat, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=date.fromisoformat, help='Second date in YYYY-MM-DD format')
    args = parser.parse_args()
    result = days_difference(args.date1, args.date2)
    print(result)