from datetime import datetime

def get_next_month(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj.month == 12:
            next_month = date_obj.replace(year=date_obj.year + 1, month=1, day=1)
        else:
            next_month = date_obj.replace(month=date_obj.month + 1, day=1)
        return next_month.strftime("%Y-%m-%d")
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return None

if __name__ == '__main__':
    sample_date1 = "2023-10-15"
    sample_date2 = "2023-12-31"
    sample_date3 = "2024-01-01"
    next_month1 = get_next_month(sample_date1)
    next_month2 = get_next_month(sample_date2)
    next_month3 = get_next_month(sample_date3)
    print(f"Next month after {sample_date1}: {next_month1}")
    print(f"Next month after {sample_date2}: {next_month2}")
    print(f"Next month after {sample_date3}: {next_month3}")