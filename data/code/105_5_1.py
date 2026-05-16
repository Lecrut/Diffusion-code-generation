import sys
from datetime import datetime, timedelta
if __name__ == '__main__':
    target_date_str = "2023-10-15"
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    if target_date.month == 12:
        next_month = target_date.replace(year=target_date.year + 1, month=1, day=1)
    else:
        next_month = target_date.replace(month=target_date.month + 1, day=1)
    print(next_month.strftime("%Y-%m-%d"))