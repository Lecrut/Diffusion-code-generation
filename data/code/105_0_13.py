import datetime

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False

def calculate_next_monday(start_date):
    start = datetime.date(start_date.year, start_date.month, start_date.day)
    days_until_monday = (7 - start.weekday()) % 7
    return start + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    start_date_str = "2023-10-15"
    if is_valid_date(start_date_str):
        start_date = datetime.date(int(start_date_str.split('-')[0]), int(start_date_str.split('-')[1]), int(start_date_str.split('-')[2]))
        next_monday = calculate_next_monday(start_date)
        print(next_monday.strftime("%Y-%m-%d"))
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")