import datetime
def is_valid_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d") is not None
    except ValueError:
        return False
if __name__ == '__main__':
    date1 = "2023-12-31"
    date2 = "2024-01-05"
    if not (is_valid_date(date1) and is_valid_date(date2)):
        print("Error: Invalid dates provided.")
        exit(1)
    try:
        dt1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        dt2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        delta_days = (dt2 - dt1).days
        print(f"Days between {date1} and {date2}: {delta_days}")
    except Exception as e:
        print(f"Runtime error occurred: {e}")