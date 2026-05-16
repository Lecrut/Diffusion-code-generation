import argparse
from datetime import datetime
def calculate_week_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    time_difference = abs(date2 - date1)
    weeks = time_difference.days / 7
    return weeks
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate the difference in weeks between two dates.")
    parser.add_argument("date1", type=str, help="The first date in YYYY-MM-DD format.")
    parser.add_argument("date2", type=str, help="The second date in YYYY-MM-DD format.")
    args = parser.parse_args(["2023-01-01", "2023-01-29"])
    result = calculate_week_difference(args.date1, args.date2)
    print(f"{result:.2f}")