import argparse
from datetime import datetime

def compare_dates(date1, date2):
    return (date1 > date2) - (date1 < date2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates.')
    parser.add_argument('date1', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), help='Second date in YYYY-MM-DD format')

    args = parser.parse_args()
    result = compare_dates(args.date1, args.date2)
    
    if result > 0:
        print(f'{args.date1.strftime("%Y-%m-%d")} is later than {args.date2.strftime("%Y-%m-%d")}')
    elif result < 0:
        print(f'{args.date1.strftime("%Y-%m-%d")} is earlier than {args.date2.strftime("%Y-%m-%d")}')
    else:
        print(f'{args.date1.strftime("%Y-%m-%d")} is the same as {args.date2.strftime("%Y-%m-%d")}')