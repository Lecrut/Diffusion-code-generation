import datetime
def is_valid_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def calculate_days_between(date1_str, date2_str):
    if not (is_valid_date(date1_str) and is_valid_date(date2_str)):
        raise ValueError("Invalid date format or impossible dates provided.")
    try:
        date_obj1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date_obj2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        delta = abs((date_obj2 - date_obj1).days)
        return delta
    except Exception:
        raise ValueError("Error calculating days between dates.")
if __name__ == '__main__':
    sample_dates_1 = "2023-04-30"
    sample_dates_2 = "2024-06-30"
    try:
        result = calculate_days_between(sample_dates_1, sample_dates_2)
        print(f"Days between {sample_dates_1} and {sample_dates_2}: {result}")
    except ValueError as e:
        print(f"Error: {e}")