import datetime
def manipulate_date():
    start_date_str = "2023-10-25"
    days_to_add = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    new_day = start_date.day + days_to_add
    if new_day > 31:
        month = start_date.month
        year = start_date.year
        while True:
            if month < 12:
                new_day -= (31 if month == 12 else 30)
                month += 1
            else:
                month = 1
                year += 1
            if new_day <= 31:
                break
    else:
        start_date = start_date.replace(day=new_day)
    result_date = start_date.strftime("%Y-%m-%d")
    print(f"Start Date: {start_date_str}")
    print(f"Days to Add: {days_to_add}")
    print(f"Resulting Date: {result_date}")
if __name__ == '__main__':
    manipulate_date()