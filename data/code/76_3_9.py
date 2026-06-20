import argparse
from datetime import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference in days between two dates.')
    parser.add_argument('date1', type=str, help='The first date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='The second date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    
    result = calculate_date_difference(args.date1, args.date2)
    print(result)