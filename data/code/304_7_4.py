import datetime
def compare_dates(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
        if date1 < date2:
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-02-20"
    try:
        result = compare_dates(date_a, date_b)
        print(f"Is {date_a} before {date_b}? {result}")
    except ValueError as e:
        print(f"Error during comparison: {e}")