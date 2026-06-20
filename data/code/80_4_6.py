import argparse
from datetime import datetime

def compare_dates(date1, date2):
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    if d1 < d2:
        return f"{date1} is earlier than {date2}"
    elif d1 > d2:
        return f"{date1} is later than {date2}"
    else:
        return f"{date1} and {date2} are the same"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compare two dates")
    parser.add_argument("date1", type=str, help="First date in YYYY-MM-DD format")
    parser.add_argument("date2", type=str, help="Second date in YYYY-MM-DD format")
    
    args = parser.parse_args()
    
    result = compare_dates(args.date1, args.date2)
    print(result)