import datetime

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        return True
    except ValueError:
        return False

def calculate_next_monday(start_date_str):
    if not is_valid_date(start_date_str):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    start_date = datetime.date(int(start_date_str.split('-')[0]), int(start_date_str.split('-')[1]), int(start_date_str.split('-')[2]))
    days_until_monday = (7 - start_date.weekday()) % 7
    next_monday = start_date + datetime.timedelta(days=days_until_monday)
    return next_monday

if __name__ == '__main__':
    sample_date = "2023-10-05"
    next_monday = calculate_next_monday(sample_date)
    print(next_monday.strftime("%Y-%m-%d"))