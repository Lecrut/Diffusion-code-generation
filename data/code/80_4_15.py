import argparse
from datetime import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Please use YYYY-MM-DD")

def compare_dates(date1, date2):
    if date1 < date2:
        return f"{date1} is strictly before {date2}"
    elif date1 > date2:
        return f"{date1} is strictly after {date2}"
    else:
        return f"{date1} and {date2} are equal"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compare two dates")
    parser.add_argument('date1', type=validate_date, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=validate_date, help='Second date in YYYY-MM-DD format')

    args = parser.parse_args()
    result = compare_dates(args.date1, args.date2)
    print(result)