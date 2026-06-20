from datetime import datetime, timedelta

def get_next_month(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    next_month = date_obj + timedelta(days=31)
    return next_month.strftime("%Y-%m-%d")

if __name__ == '__main__':
    sample_date1 = "2023-10-15"
    sample_date2 = "2023-12-31"
    print(f"Next month after {sample_date1}: {get_next_month(sample_date1)}")
    print(f"Next month after {sample_date2}: {get_next_month(sample_date2)}")