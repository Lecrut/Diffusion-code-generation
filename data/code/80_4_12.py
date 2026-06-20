import argparse
from datetime import datetime

def compare_dates(date1, date2):
    return date1 < date2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates.')
    parser.add_argument('date1', type=datetime.fromisoformat, help='First date in ISO format')
    parser.add_argument('date2', type=datetime.fromisoformat, help='Second date in ISO format')

    args = parser.parse_args()
    
    result = compare_dates(args.date1, args.date2)
    print(f"Is {args.date1} strictly before {args.date2}? {result}")