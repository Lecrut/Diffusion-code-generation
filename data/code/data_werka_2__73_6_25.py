import datetime
import time

def date_difference(date1_str: str, date2_str: str) -> datetime.timedelta:
    fmt = "%Y-%m-%d"
    d1 = datetime.datetime.strptime(date1_str, fmt).date()
    d2 = datetime.datetime.strptime(date2_str, fmt).date()
    return d2 - d1

if __name__ == '__main__':
    result = date_difference("2023-01-01", "2023-12-31")
    print(result)