import sys
from datetime import datetime, timedelta
if __name__ == '__main__':
    target_date_str = "2023-10-15"
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    if target_date.month == 12:
        next_month_year = target_date.year + 1
        next_month = 1
    else:
        next_month_year = target_date.year
        next_month = target_date.month + 1
    if next_month == 13:
        next_month = 1
        next_month_year += 1
    next_month_date = datetime(next_month_year, next_month, 1)
    next_full_month = next_month_date + timedelta(days=31)
    print(next_full_month.strftime("%Y-%m-%d"))