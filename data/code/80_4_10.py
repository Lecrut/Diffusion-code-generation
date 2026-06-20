import argparse
from datetime import datetime

def compare_dates(date1, date2):
    if date1 > date2:
        return f"{date1} is later than {date2}"
    elif date1 < date2:
        return f"{date1} is earlier than {date2}"
    else:
        return f"{date1} and {date2} are the same"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates')
    parser.add_argument('date1', type=datetime.strptime, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=datetime.strptime, help='Second date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    
    result = compare_dates(args.date1, args.date2)
    print(result)