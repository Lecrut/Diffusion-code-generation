from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def days_difference(date1_str, date2_str):
    if not (validate_date(date1_str) and validate_date(date2_str)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date1_obj = datetime.strptime(date1_str, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2_str, '%Y-%m-%d')
    delta = abs((date2_obj - date1_obj).days)
    return delta

if __name__ == '__main__':
    date1_sample = "2023-10-01"
    date2_sample = "2023-10-15"
    print(f"Days between {date1_sample} and {date2_sample}: {days_difference(date1_sample, date2_sample)}")