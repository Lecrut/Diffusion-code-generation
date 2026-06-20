import datetime

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def contains_weekday(date_list):
    if not all(is_valid_date(date) for date in date_list):
        raise ValueError("All items in the list must be valid dates.")
    return any(datetime.datetime.strptime(date, "%Y-%m-%d").weekday() < 5 for date in date_list)

if __name__ == '__main__':
    dates = ["2023-10-27", "2024-02-29", "2023-10-28", "2023-02-28"]
    print(f"Contains weekday: {contains_weekday(dates)}")