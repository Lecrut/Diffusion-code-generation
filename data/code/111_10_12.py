from datetime import datetime

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def days_difference():
    date1 = "2023-10-01"
    date2 = "2023-10-15"
    
    if not (validate_date_format(date1) and validate_date_format(date2)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')
    delta = abs((date2_obj - date1_obj).days)
    return delta

if __name__ == '__main__':
    print(f"Days between 2023-10-01 and 2023-10-15: {days_difference()}")