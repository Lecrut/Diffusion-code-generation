import argparse
from datetime import date
def compare_dates(date_str1, date_str2):
    date1 = date.fromisoformat(date_str1)
    date2 = date.fromisoformat(date_str2)
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
    args = parser.parse_args(["2023-10-26", "2023-10-25"])
    compare_dates(args.date1, args.date2)