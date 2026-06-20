from datetime import datetime

def is_date_before(date_str1: str, date_str2: str) -> bool:
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except ValueError:
        print("Error: Invalid date format provided.", file=sys.stderr)
        return False
    
    return date1 < date2

if __name__ == '__main__':
    date_str1 = "2023-10-26"
    date_str2 = "2023-10-20"
    
    result = is_date_before(date_str1, date_str2)
    print(result)