from datetime import datetime

def get_next_month(date_str):
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    if current_date.month == 12:
        next_month = current_date.replace(year=current_date.year + 1, month=1, day=1)
    else:
        next_month = current_date.replace(month=current_date.month + 1, day=1)
    return next_month.strftime("%Y-%m-%d")

if __name__ == '__main__':
    sample_date1 = "2023-10-15"
    sample_date2 = "2023-12-31"
    sample_date3 = "2024-01-01"
    print(f"Next month after {sample_date1}: {get_next_month(sample_date1)}")
    print(f"Next month after {sample_date2}: {get_next_month(sample_date2)}")
    print(f"Next month after {sample_date3}: {get_next_month(sample_date3)}")