import sys
from datetime import datetime, timedelta
if __name__ == '__main__':
    input_date_str = "2023-10-15"
    input_date = datetime.strptime(input_date_str, "%Y-%m-%d")
    if input_date.month == 12:
        next_month_start = input_date.replace(year=input_date.year + 1, month=1, day=1)
    else:
        next_month_start = input_date.replace(month=input_date.month + 1, day=1)
    output_date = next_month_start
    print(output_date.strftime("%Y-%m-%d"))