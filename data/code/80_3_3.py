import sys
from datetime import datetime
def solve():
    date_str1 = "2023-01-15"
    date_str2 = "2023-03-01"
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except ValueError:
        print("Error: Invalid date format provided.", file=sys.stderr)
        return
    if date1 < date2:
        ordered_pair = (date1, date2)
    else:
        ordered_pair = (date2, date1)
    print(f"Chronologically ordered pair: ({ordered_pair[0].strftime(date_format)}, {ordered_pair[1].strftime(date_format)})")
if __name__ == '__main__':
    solve()