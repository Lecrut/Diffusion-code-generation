from datetime import datetime

def compare_dates(date_str1: str, date_str2: str) -> str:
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    if date1 < date2:
        return "date1 is earlier than date2"
    elif date1 > date2:
        return "date1 is later than date2"
    else:
        return "date1 and date2 are the same"

if __name__ == '__main__':
    print(compare_dates("2023-04-01", "2023-05-01"))
    print(compare_dates("2023-06-01", "2023-05-01"))
    print(compare_dates("2023-05-01", "2023-05-01"))