import argparse
from datetime import datetime

def compare_dates(date1, date2):
    return date1 < date2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates.')
    parser.add_argument('date1', type=str, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='Second date in YYYY-MM-DD format')

    args = parser.parse_args()

    date_a = datetime.strptime(args.date1, '%Y-%m-%d')
    date_b = datetime.strptime(args.date2, '%Y-%m-%d')

    print(f"Is {args.date1} strictly before {args.date2}? {compare_dates(date_a, date_b)}")