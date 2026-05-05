import argparse
from datetime import date
def compare_dates(date_str1, date_str2):
    try:
        date1 = date.fromisoformat(date_str1)
        date2 = date.fromisoformat(date_str2)
        if date1 > date2:
            print(f"{date_str1} is after {date_str2}")
        elif date1 < date2:
            print(f"{date_str1} is before {date_str2}")
        else:
            print(f"{date_str1} is the same as {date_str2}")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compare two dates.")
    parser.add_argument("date1", type=str, help="The first date in YYYY-MM-DD format.")
    parser.add_argument("date2", type=str, help="The second date in YYYY-MM-DD format.")
    args = parser.parse_args(["2023-01-15", "2023-01-20"])
    compare_dates(args.date1, args.date2)