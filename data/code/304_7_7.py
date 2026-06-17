import datetime
def compare_dates(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        if date1 < date2:
            return True
        else:
            return False
    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use YYYY-MM-DD. Error: {e}")
if __name__ == '__main__':
    date_str1 = "2023-01-15"
    date_str2 = "2023-02-20"
    try:
        is_before = compare_dates(date_str1, date_str2)
        if is_before:
            print(f"{date_str1} is before {date_str2}")
        else:
            print(f"{date_str1} is not before {date_str2}")
    except ValueError as e:
        print(f"Error during date comparison: {e}")