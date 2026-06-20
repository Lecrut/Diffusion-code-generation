from datetime import datetime

def is_strictly_before(date1: datetime, date2: datetime) -> bool:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Both arguments must be instances of datetime.")
    return date1 < date2

if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-20"
    date_format = "%Y-%m-%d"
    
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except ValueError:
        print("Error: Invalid date format provided.")
        exit(1)
    
    result = is_strictly_before(date1, date2)
    print(result)