import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_next_month(date_str):
    if not validate_date(date_str):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    next_month = date_obj.replace(day=1) + datetime.timedelta(days=32)
    return next_month.replace(day=1)

if __name__ == '__main__':
    sample_date = "2023-10-15"
    print(f"Original Date: {sample_date}")
    print(f"Next Month's Date: {get_next_month(sample_date)}")
    
    sample_date_dec = "2023-12-31"
    print(f"Original Date: {sample_date_dec}")
    print(f"Next Month's Date: {get_next_month(sample_date_dec)}")