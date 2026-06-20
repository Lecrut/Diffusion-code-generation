from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_next_month_first_day(date_obj):
    if date_obj.month == 12:
        next_year = date_obj.year + 1
        next_month = 1
    else:
        next_year = date_obj.year
        next_month = date_obj.month + 1
    
    return datetime(next_year, next_month, 1)

def get_next_month_date(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")
    
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return get_next_month_first_day(date_obj).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = "2024-03-31"
    result = get_next_month_date(sample_date)
    print(result)