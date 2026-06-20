import argparse
from datetime import datetime

def date_difference(date1, date2):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = abs((b - a).days)
    return delta

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference in days between two dates.')
    parser.add_argument('date1', type=str, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='Second date in YYYY-MM-DD format')
    args = parser.parse_args()
    print(date_difference(args.date1, args.date2))