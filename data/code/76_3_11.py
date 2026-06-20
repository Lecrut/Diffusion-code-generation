import argparse
from datetime import datetime

def date_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference in days between two dates.')
    parser.add_argument('date1', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), help='Second date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    result = date_difference(args.date1, args.date2)
    print(result)