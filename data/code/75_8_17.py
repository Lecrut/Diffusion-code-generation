import datetime

def validate_date_format(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_days_between_dates(date_str1, date_str2):
    if not (validate_date_format(date_str1) and validate_date_format(date_str2)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d").date()
    
    if date1 > date2:
        start_date = date2
        end_date = date1
    else:
        start_date = date1
        end_date = date2
    
    time_difference = end_date - start_date
    return time_difference.days

if __name__ == '__main__':
    date_str1 = "2023-01-15"
    date_str2 = "2021-11-20"
    
    days_between = calculate_days_between_dates(date_str1, date_str2)
    print(f"Total Days: {days_between}")