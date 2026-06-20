from datetime import datetime

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def calculate_date_difference(date1_str, date2_str):
    if not (validate_date_format(date1_str) and validate_date_format(date2_str)):
        raise ValueError("Both dates must be in the format YYYY-MM-DD")
    
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-10"
    difference = calculate_date_difference(date1, date2)
    print(difference)