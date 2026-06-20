from datetime import datetime

def validate_date_format(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def compare_dates(date_str1: str, date_str2: str) -> int:
    if not validate_date_format(date_str1) or not validate_date_format(date_str2):
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    result = compare_dates('2023-04-01', '2023-05-01')
    print(result)