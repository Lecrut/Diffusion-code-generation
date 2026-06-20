import datetime

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_days_in_month(year, month):
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    first_day_of_next_month = datetime.date(next_month[0], next_month[1], 1)
    return (first_day_of_next_month - datetime.timedelta(days=1)).day

def calculate_remaining_days(current_date_str, target_date_str):
    if not is_valid_date(current_date_str) or not is_valid_date(target_date_str):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    
    if target_date < current_date:
        return 0
    
    days_in_current_month = get_days_in_month(current_date.year, current_date.month)
    remaining_days = days_in_current_month - current_date.day + (target_date - datetime.date(target_date.year, target_date.month, 1)).days
    
    return remaining_days

if __name__ == '__main__':
    current_date = "2023-10-15"
    target_date = "2023-11-15"
    days_left = calculate_remaining_days(current_date, target_date)
    print(days_left)