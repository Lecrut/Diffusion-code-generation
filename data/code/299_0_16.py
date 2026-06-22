from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_weekend(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() >= 5

if __name__ == '__main__':
    print(is_weekend('2023-10-07'))
    print(is_weekend('2023-10-08'))
    print(is_weekend('2023-10-09'))