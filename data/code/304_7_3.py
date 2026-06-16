def compare_dates(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        if date1 < date2:
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
import datetime
if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-02-20"
    try:
        is_before = compare_dates(date1_input, date2_input)
        print(f"Is {date1_input} before {date2_input}? {is_before}")
    except ValueError as e:
        print(f"Error during comparison: {e}")