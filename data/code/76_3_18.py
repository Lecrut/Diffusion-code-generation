import argparse
from datetime import datetime

def date_difference(date1, date2):
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    delta = abs((d2 - d1).days)
    return delta

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference in days between two dates.')
    parser.add_argument('date1', type=str, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='Second date in YYYY-MM-DD format')
    args = parser.parse_args()
    
    result = date_difference(args.date1, args.date2)
    print(result)