import datetime

def is_date_weekend(date_str):
    try:
        date = datetime.datetime.strptime(str(date_str), '%Y-%m-%d').date()
        return date.weekday() >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please provide the date in YYYY-MM-DD format.")

if __name__ == '__main__':
    dates = [
        "2023-10-28",
        "2023-10-29",
        "2023-10-30",
        "2023-10-31",
        "2023-11-05"
    ]
    
    for date in dates:
        try:
            print(f"{date} is weekend: {is_date_weekend(date)}")
        except ValueError as e:
            print(e)