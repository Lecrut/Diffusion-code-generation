import argparse
from datetime import datetime

def compare_dates(date1, date2):
    return (date1 > date2) - (date1 < date2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates.')
    parser.add_argument('date1', type=str, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='Second date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    
    date_format = '%Y-%m-%d'
    try:
        date1_obj = datetime.strptime(args.date1, date_format)
        date2_obj = datetime.strptime(args.date2, date_format)
        
        result = compare_dates(date1_obj, date2_obj)
        if result > 0:
            print(f'{args.date1} is later than {args.date2}')
        elif result < 0:
            print(f'{args.date1} is earlier than {args.date2}')
        else:
            print(f'{args.date1} and {args.date2} are the same')
    except ValueError as e:
        print(f'Invalid date format: {e}')