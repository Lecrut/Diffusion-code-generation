from datetime import datetime

def get_next_month(date_str):
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    if current_date.month == 12:
        next_month = current_date.replace(year=current_date.year + 1, month=1, day=1)
    else:
        next_month = current_date.replace(month=current_date.month + 1, day=1)
    return next_month.strftime("%Y-%m-%d")

if __name__ == '__main__':
    sample_date = "2023-11-15"
    next_month = get_next_month(sample_date)
    print(f"The next month after {sample_date} is {next_month}")