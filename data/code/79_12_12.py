from datetime import datetime, timedelta

def get_next_month(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    if date_obj.month == 12:
        next_month = date_obj.replace(year=date_obj.year + 1, month=1)
    else:
        next_month = date_obj.replace(month=date_obj.month + 1)
    return next_month.strftime("%Y-%m-%d")

if __name__ == '__main__':
    sample_date = "2023-10-15"
    next_month = get_next_month(sample_date)
    print(f"The next month after {sample_date} is {next_month}")