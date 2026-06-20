import argparse
from datetime import date

def validate_date(date_str):
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format, should be YYYY-MM-DD")

def days_difference(date1, date2):
    earlier_date = min(date1, date2)
    later_date = max(date1, date2)
    return (later_date - earlier_date).days

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference in days between two dates.")
    parser.add_argument('date1', type=validate_date, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=validate_date, help='Second date in YYYY-MM-DD format')

    args = parser.parse_args()
    
    result = days_difference(args.date1, args.date2)
    print(result)

if __name__ == '__main__':
    main()