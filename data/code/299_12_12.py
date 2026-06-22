import datetime

def is_weekend(date_input):
    try:
        date = datetime.datetime.strptime(str(date_input), '%Y-%m-%d').date()
        weekday = date.weekday()
        return weekday >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    dates_to_check = ["2023-10-28", "2023-10-29", "2023-10-30", "2023-10-31", "2023-11-05"]
    for date in dates_to_check:
        print(f"{date} is weekend: {is_weekend(date)}")