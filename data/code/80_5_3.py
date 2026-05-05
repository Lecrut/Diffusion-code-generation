import argparse
from datetime import datetime
def compare_dates(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")
    if date1 > date2:
        print(f"{date_str1} is after {date_str2}")
    elif date1 < date2:
        print(f"{date_str1} is before {date_str2}")
    else:
        print(f"{date_str1} is the same as {date_str2}")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("date1", type=str, help="The first date in YYYY-MM-DD format")
    parser.add_argument("date2", type=str, help="The second date in YYYY-MM-DD format")
    args = parser.parse_args(["2023-01-15", "2023-01-15"])
    compare_dates(args.date1, args.date2)