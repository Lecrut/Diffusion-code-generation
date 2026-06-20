from datetime import datetime

DATE_FORMAT = "%m/%d/%Y"

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False

def calculate_difference(date_str1, date_str2):
    if not (is_valid_date(date_str1) and is_valid_date(date_str2)):
        raise ValueError("Invalid date format. Please use MM/DD/YYYY.")
    
    date1 = datetime.strptime(date_str1, DATE_FORMAT)
    date2 = datetime.strptime(date_str2, DATE_FORMAT)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    try:
        difference = calculate_difference('01/01/2023', '01/10/2023')
        print(difference)
    except ValueError as e:
        print(e)