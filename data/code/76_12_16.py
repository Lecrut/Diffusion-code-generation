from datetime import datetime

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

def calculate_date_difference(date_str1, date_str2):
    if not (validate_date_format(date_str1) and validate_date_format(date_str2)):
        raise ValueError("Both dates must be in the correct format.")
    
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    difference = abs((date2 - date1).days)
    return difference

if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-28"
    
    try:
        difference = calculate_date_difference(date1_str, date2_str)
        print(f"Date 1: {date1_str}")
        print(f"Date 2: {date2_str}")
        print(f"The difference between the two dates is {difference} days.")
    except ValueError as e:
        print(e)