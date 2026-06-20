from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def calculate_difference(date_str1, date_str2):
    if not (is_valid_date(date_str1) and is_valid_date(date_str2)):
        raise ValueError("Both dates must be in MM/DD/YYYY format.")
    
    date1 = datetime.strptime(date_str1, '%m/%d/%Y')
    date2 = datetime.strptime(date_str2, '%m/%d/%Y')
    
    return abs((date2 - date1).days)

if __name__ == '__main__':
    result = calculate_difference('01/01/2023', '10/01/2023')
    print(result)