import argparse
from datetime import datetime

def compare_dates(date1, date2):
    if date1 < date2:
        return f"{date1} is strictly before {date2}"
    elif date2 < date1:
        return f"{date2} is strictly before {date1}"
    else:
        return f"{date1} and {date2} are the same"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates.')
    parser.add_argument('date1', type=datetime.fromisoformat, help='First date in ISO format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('date2', type=datetime.fromisoformat, help='Second date in ISO format (YYYY-MM-DDTHH:MM:SS)')

    args = parser.parse_args()

    result = compare_dates(args.date1, args.date2)
    print(result)