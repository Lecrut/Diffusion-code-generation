import argparse
from datetime import datetime
DAYS_IN_WEEK = 7

def date_to_ordinal(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').toordinal()

def weeks_difference(date1_str, date2_str):
    ordinal1 = date_to_ordinal(date1_str)
    ordinal2 = date_to_ordinal(date2_str)
    difference = abs(ordinal1 - ordinal2)
    return difference // DAYS_IN_WEEK
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference in weeks between two dates.')
    parser.add_argument('date1', type=str, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='Second date in YYYY-MM-DD format')
    args = parser.parse_args()
    result = weeks_difference(args.date1, args.date2)
    print(result)