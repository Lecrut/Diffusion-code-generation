from datetime import datetime

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_year_difference(date_str1, date_str2):
    if not (validate_date_format(date_str1) and validate_date_format(date_str2)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    date1 = "2020-01-01"
    date2 = "1995-01-01"
    difference = calculate_year_difference(date1, date2)
    print(difference)