import sys
from datetime import datetime
def solve():
    date_str1 = "2023-01-15"
    date_str2 = "2022-12-31"
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except ValueError:
        print("Error: Invalid date format provided.")
        return
    if date1 < date2:
        ordered_date1 = date1
        ordered_date2 = date2
    else:
        ordered_date1 = date2
        ordered_date2 = date1
    print(f"{ordered_date1} {ordered_date2}")
if __name__ == '__main__':
    solve()