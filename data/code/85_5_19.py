import argparse
from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def weeks_difference(date1, date2):
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate the difference in weeks between two dates.")
    parser.add_argument("date1", type=str, help="The first date in YYYY-MM-DD format.")
    parser.add_argument("date2", type=str, help="The second date in YYYY-MM-DD format.")
    
    args = parser.parse_args()
    
    date1_obj = parse_date(args.date1)
    date2_obj = parse_date(args.date2)
    
    result = weeks_difference(date1_obj, date2_obj)
    print(result)