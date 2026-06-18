import datetime
def is_valid_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    sample_dates = ["2023-12-31", "2024-02-30", "invalid-date"]
    for date_str in sample_dates:
        if is_valid_date(date_str):
            print(f"{date_str} is valid")
        else:
            print(f"{date_str} is invalid or impossible")