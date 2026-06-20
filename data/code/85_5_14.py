import argparse
from datetime import date

def parse_date(date_str):
    return date.fromisoformat(date_str)

def calculate_weeks_difference(date1, date2):
    delta = abs((date1 - date2).days)
    return delta // 7

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate weeks difference between two dates.')
    parser.add_argument('date1', type=parse_date, help='First date in ISO format (YYYY-MM-DD)')
    parser.add_argument('date2', type=parse_date, help='Second date in ISO format (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    result = calculate_weeks_difference(args.date1, args.date2)
    print(result)