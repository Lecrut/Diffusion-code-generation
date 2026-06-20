import argparse
from datetime import datetime

def compare_dates(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    if date1 < date2:
        return f'{date_str1} is earlier than {date_str2}'
    elif date1 > date2:
        return f'{date_str1} is later than {date_str2}'
    else:
        return f'{date_str1} and {date_str2} are the same'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare two dates.')
    parser.add_argument('date1', type=str, help='First date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='Second date in YYYY-MM-DD format')
    args = parser.parse_args()
    result = compare_dates(args.date1, args.date2)
    print(result)