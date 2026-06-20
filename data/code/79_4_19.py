from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def first_day_of_next_month(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Invalid date format. Please provide date in 'YYYY-MM-DD' format.")
    
    current_date = datetime.strptime(date_str, '%Y-%m-%d')
    next_month_first_day = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1)
    return next_month_first_day.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date_str = "2023-10-15"
    print(first_day_of_next_month(sample_date_str))