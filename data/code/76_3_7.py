import argparse
from datetime import date

def days_difference(date1: date, date2: date) -> int:
    earlier_date = min(date1, date2)
    later_date = max(date1, date2)
    return (later_date - earlier_date).days

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate the difference in days between two dates.")
    parser.add_argument("date1", type=date.fromisoformat, help="First date in YYYY-MM-DD format")
    parser.add_argument("date2", type=date.fromisoformat, help="Second date in YYYY-MM-DD format")

    args = parser.parse_args()

    result = days_difference(args.date1, args.date2)
    print(result)