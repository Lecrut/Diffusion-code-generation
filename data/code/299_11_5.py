import datetime
def is_weekend(date_input):
    if isinstance(date_input, datetime.date) or isinstance(date_input, datetime.datetime):
        date = date_input.date() if isinstance(date_input, datetime.datetime) else date_input
    elif isinstance(date_input, str):
        try:
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            return False
    else:
        return False
    day_of_week = date.weekday()
    return day_of_week >= 5
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 1)
    date2 = datetime.date(2023, 10, 7)
    date3_str = "2023-10-08"
    date4_str = "2023-10-09"
    date5_invalid = "2023-10-00"
    print(f"Date {date1}: {is_weekend(date1)}")
    print(f"Date {date2}: {is_weekend(date2)}")
    print(f"Date string '{date3_str}': {is_weekend(date3_str)}")
    print(f"Date string '{date4_str}': {is_weekend(date4_str)}")
    print(f"Invalid date string '{date5_invalid}': {is_weekend(date5_invalid)}")