import argparse
from datetime import datetime

def compare_dates(date1_str, date2_str):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return date1 < date2
    except ValueError as e:
        print(f"Invalid date format. Please use {date_format}.")
        raise

def main():
    parser = argparse.ArgumentParser(description="Compare two dates.")
    parser.add_argument("date1", type=str, help="First date in YYYY-MM-DD format")
    parser.add_argument("date2", type=str, help="Second date in YYYY-MM-DD format")

    args = parser.parse_args()

    result = compare_dates(args.date1, args.date2)
    print(f"Is {args.date1} strictly before {args.date2}? {result}")

if __name__ == '__main__':
    main()