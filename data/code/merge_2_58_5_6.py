import datetime
def is_valid_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    dates = ["2023-10-31", "2024-02-30", "invalid-date"]
    for d in dates:
        if is_valid_date(d):
            print(f"Valid date found")
        else:
            try:
                datetime.datetime.strptime(d, "%Y-%m-%d")
            except ValueError as e:
                pass