import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def calculate_week_difference(date_str1, date_str2):
    if not (validate_date(date_str1) and validate_date(date_str2)):
        raise ValueError("Both dates must be in 'YYYY-MM-DD' format.")
    
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    time_difference = abs(date2 - date1)
    weeks = time_difference.days / 7.0
    return weeks

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-08"
    result = calculate_week_difference(date1, date2)
    print(result)