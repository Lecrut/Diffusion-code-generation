import argparse
from datetime import date
def calculate_difference(date1_str, date2_str):
    date1 = date.fromisoformat(date1_str)
    date2 = date.fromisoformat(date2_str)
    return abs((date2 - date1).days)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('date1', type=str, help='The first date in YYYY-MM-DD format')
    parser.add_argument('date2', type=str, help='The second date in YYYY-MM-DD format')
    args = parser.parse_args(['2023-01-01', '2023-01-10'])
    difference = calculate_difference(args.date1, args.date2)
    print(difference)