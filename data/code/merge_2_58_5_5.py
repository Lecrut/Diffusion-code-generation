import datetime
def is_valid_date(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def calculate_days_between(start_str, end_str):
    if not (is_valid_date(start_str) and is_valid_date(end_str)):
        raise ValueError("Invalid date format or impossible dates provided.")
    start_dt = datetime.datetime.strptime(start_str, "%Y-%m-%d")
    end_dt = datetime.datetime.strptime(end_str, "%Y-%m-%d")
    days_difference = (end_dt - start_dt).days
    return abs(days_difference)
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-02-30"]                               
    try:
        result = calculate_days_between(sample_dates[0], sample_dates[1])
        print(f"Days between dates: {result}")
    except ValueError as e:
        print(f"Error: {e}")