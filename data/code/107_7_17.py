import datetime

def validate_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def date_to_iso(date_string):
    if not validate_date_format(date_string):
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
    dt_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return dt_object.strftime('%Y-%m-%dT%H:%M:%SZ')

if __name__ == '__main__':
    date_str1 = "2023-10-27"
    print(f"{date_str1}: {date_to_iso(date_str1)}")
    
    date_str2 = "1999-01-01"
    print(f"{date_str2}: {date_to_iso(date_str2)}")